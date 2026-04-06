# TCS Digital Interview - SQL Practice Guide

## 1. SQL FUNDAMENTALS FOR INTERVIEWS

### Basic SELECT Statement
```sql
-- Simple SELECT
SELECT * FROM employees;
SELECT name, salary FROM employees;

-- SELECT with WHERE clause
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'IT' AND salary > 50000;
```

---

## 2. COMMON SQL QUERIES

### Q1: Retrieve Employees with Salary Above Average
```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;
```

**Explanation:**
- Inner query calculates average salary
- Outer query filters employees above that average
- Subqueries are powerful for complex filtering

---

### Q2: Get Department-wise Employee Count
```sql
SELECT 
    department,
    COUNT(*) as employee_count,
    AVG(salary) as average_salary
FROM employees
GROUP BY department
ORDER BY employee_count DESC;
```

**Key Concepts:**
- `GROUP BY`: Groups data by column(s)
- `COUNT()`: Counts rows
- `AVG()`: Calculates average
- `ORDER BY`: Sorts result

---

### Q3: Find Departments with More than 5 Employees
```sql
SELECT 
    department,
    COUNT(*) as emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

**Difference from WHERE:**
- `WHERE`: Filters rows BEFORE grouping
- `HAVING`: Filters groups AFTER grouping

---

### Q4: Join Multiple Tables
```sql
-- INNER JOIN - Only matching records
SELECT 
    e.name,
    e.salary,
    d.department_name,
    m.manager_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id
LEFT JOIN managers m ON d.manager_id = m.id
ORDER BY e.salary DESC;
```

**JOIN Types:**
- `INNER JOIN`: Only rows with matches in both tables
- `LEFT JOIN`: All rows from left table + matches from right
- `RIGHT JOIN`: All rows from right table + matches from left
- `FULL OUTER JOIN`: All rows from both tables
- `CROSS JOIN`: Cartesian product of both tables

---

### Q5: Find Top N Highest Paid Employees
```sql
-- Using LIMIT
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;

-- Using DENSE_RANK (works better with ties)
SELECT 
    name,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as rank
FROM employees
WHERE DENSE_RANK() OVER (ORDER BY salary DESC) <= 5;
```

---

### Q6: Get Duplicate Records
```sql
SELECT 
    email,
    COUNT(*) as count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

---

### Q7: Delete Duplicate Records (Keep one)
```sql
DELETE FROM users
WHERE id NOT IN (
    SELECT MIN(id)
    FROM users
    GROUP BY email
);
```

---

### Q8: Find Missing IDs in Sequence
```sql
SELECT id + 1 as missing_id
FROM employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM employees
    WHERE id = e.id + 1
)
AND id < (SELECT MAX(id) FROM employees);
```

---

### Q9: Get Running Total
```sql
SELECT 
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as running_total
FROM orders
ORDER BY order_date;
```

---

### Q10: Rank Within Groups
```sql
SELECT 
    department,
    name,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) as dept_salary_rank
FROM employees;
```

---

## 3. WINDOW FUNCTIONS

### Common Window Functions:

```sql
-- ROW_NUMBER: Unique number for each row
SELECT 
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
FROM employees;

-- RANK: Same rank for ties, gaps in numbering
SELECT 
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- DENSE_RANK: Same rank for ties, no gaps
SELECT 
    name,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;

-- LAG: Access previous row value
SELECT 
    order_date,
    amount,
    LAG(amount) OVER (ORDER BY order_date) as prev_amount
FROM orders;

-- LEAD: Access next row value
SELECT 
    order_date,
    amount,
    LEAD(amount) OVER (ORDER BY order_date) as next_amount
FROM orders;

-- FIRST_VALUE / LAST_VALUE
SELECT 
    department,
    name,
    salary,
    FIRST_VALUE(salary) OVER (PARTITION BY department ORDER BY salary DESC) as highest_in_dept,
    LAST_VALUE(salary) OVER (PARTITION BY department ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as lowest_in_dept
FROM employees;
```

---

## 4. COMMON INTERVIEW PROBLEMS

### Problem 1: Second Highest Salary
```sql
-- Method 1: Using DISTINCT and LIMIT
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Method 2: Using MAX and subquery
SELECT MAX(salary) as second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Method 3: Using DENSE_RANK
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank
    FROM employees
) ranked
WHERE rank = 2;
```

---

### Problem 2: Employees Earning More Than Their Manager
```sql
SELECT 
    e.name as employee,
    e.salary as emp_salary,
    m.name as manager,
    m.salary as manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

---

### Problem 3: Consecutive Dates with Sales
```sql
SELECT 
    order_date,
    amount,
    COUNT(*) OVER (
        ORDER BY order_date
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) as consecutive_count
FROM orders
WHERE amount > 100
ORDER BY order_date;
```

---

### Problem 4: Department with Highest Average Salary
```sql
SELECT 
    department,
    AVG(salary) as avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;
```

---

### Problem 5: Employees in Same Department Earning More Than Average
```sql
SELECT 
    name,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY department, salary DESC;
```

---

## 5. PERFORMANCE OPTIMIZATION TIPS

### Indexes
```sql
-- Create index for faster searches
CREATE INDEX idx_employees_salary ON employees(salary);
CREATE INDEX idx_employees_dept_salary ON employees(department, salary);

-- Check existing indexes
SHOW INDEX FROM employees;

-- Drop unused index
DROP INDEX idx_employees_salary ON employees;
```

### Query Optimization Techniques
1. **Use indexes on frequently searched columns**
2. **Use EXPLAIN to analyze query performance**
3. **Avoid SELECT * when not needed**
4. **Use INNER JOIN instead of multiple WHERE conditions when possible**
5. **Limit result set with WHERE clause early**
6. **Use column-specific queries**

```sql
-- BAD: Gets all columns and then filters
SELECT * FROM employees WHERE salary > 50000;

-- GOOD: Gets only needed columns
SELECT name, salary FROM employees WHERE salary > 50000;
```

---

## 6. STRING OPERATIONS

```sql
-- Concatenation
SELECT CONCAT(first_name, ' ', last_name) as full_name
FROM employees;

-- Substring
SELECT SUBSTRING(name, 1, 3) as first_three
FROM employees;

-- Length
SELECT name, LENGTH(name) as name_length
FROM employees;

-- Upper/Lower case
SELECT UPPER(name), LOWER(name)
FROM employees;

-- Trim spaces
SELECT TRIM(name)
FROM employees;

-- Pattern matching
SELECT * FROM employees WHERE name LIKE 'A%';  -- Starts with A
SELECT * FROM employees WHERE name LIKE '%son';  -- Ends with 'son'
SELECT * FROM employees WHERE name LIKE '%john%';  -- Contains 'john'
```

---

## 7. DATE OPERATIONS

```sql
-- Current date/time
SELECT NOW(), CURDATE(), CURTIME();

-- Extract parts
SELECT YEAR(hire_date), MONTH(hire_date), DAY(hire_date)
FROM employees;

-- Date formatting
SELECT DATE_FORMAT(hire_date, '%Y-%m-%d') as formatted_date
FROM employees;

-- Date arithmetic
SELECT 
    name,
    hire_date,
    DATE_ADD(hire_date, INTERVAL 5 YEAR) as promotion_eligible_date
FROM employees;

-- Days between dates
SELECT 
    name,
    DATEDIFF(CURDATE(), hire_date) as days_employed
FROM employees;
```

---

## 8. AGGREGATE FUNCTIONS

```sql
-- COUNT: Number of non-NULL values
SELECT COUNT(salary) FROM employees;

-- SUM: Total of numeric values
SELECT SUM(salary) FROM employees;

-- AVG: Average of numeric values
SELECT AVG(salary) FROM employees;

-- MIN/MAX: Minimum and maximum values
SELECT MIN(salary), MAX(salary) FROM employees;

-- GROUP_CONCAT: Combine values
SELECT department, GROUP_CONCAT(name) as employees
FROM employees
GROUP BY department;
```

---

## 9. CASE STATEMENTS

```sql
-- Simple CASE
SELECT 
    name,
    salary,
    CASE 
        WHEN salary < 30000 THEN 'Junior'
        WHEN salary < 60000 THEN 'Senior'
        ELSE 'Lead'
    END as level
FROM employees;

-- CASE with searched condition
SELECT 
    name,
    salary,
    CASE 
        WHEN status = 'active' AND salary > 50000 THEN 'Active High Earner'
        WHEN status = 'active' THEN 'Active'
        ELSE 'Inactive'
    END as category
FROM employees;
```

---

## 10. COMMONLY ASKED SQL IN INTERVIEWS

### Q1: Write query to find employees hired in 2023
```sql
SELECT * FROM employees
WHERE YEAR(hire_date) = 2023;
```

### Q2: Get list of employees and their department salary ranking
```sql
SELECT 
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees;
```

### Q3: Find departments where average salary is higher than company average
```sql
SELECT 
    department,
    AVG(salary) as dept_avg
FROM employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees)
ORDER BY dept_avg DESC;
```

### Q4: List employees and count of projects they work on
```sql
SELECT 
    e.name,
    COUNT(p.id) as project_count
FROM employees e
LEFT JOIN project_assignments pa ON e.id = pa.employee_id
LEFT JOIN projects p ON pa.project_id = p.id
GROUP BY e.id, e.name
ORDER BY project_count DESC;
```

### Q5: Find employees with no assigned projects
```sql
SELECT * FROM employees e
WHERE NOT EXISTS (
    SELECT 1 FROM project_assignments pa
    WHERE pa.employee_id = e.id
);
```

---

## 11. SQL BEST PRACTICES FOR INTERVIEWS

✅ **DO:**
- Use meaningful table and column aliases
- Write readable, well-formatted queries
- Include comments for complex logic
- Test queries with edge cases
- Optimize queries when possible
- Explain your approach before writing

❌ **DON'T:**
- Use SELECT * without specific need
- Forget to handle NULL values
- Create queries without WHERE clause (unless intended)
- Use complex nested subqueries when JOINs would work
- Forget to consider performance
- Miss out on explaining your logic

---

## 12. PRACTICE RESOURCES

1. **LeetCode** - Database problems (specific SQL problems)
2. **HackerRank** - SQL practice tracks
3. **Codewars** - SQL katas
4. **W3Schools** - SQL tutorial and interactive editor
5. **Mode Analytics** - SQL tutorial with business context

---

## 13. QUICK SYNTAX REFERENCE

```sql
SELECT column1, column2          -- Columns to retrieve
FROM table_name                  -- Table to query
JOIN other_table ON condition    -- Join with other table
WHERE condition                  -- Filter rows
GROUP BY column                  -- Group by column
HAVING condition                 -- Filter groups
ORDER BY column                  -- Sort results
LIMIT n;                         -- Limit rows returned
```

---

**Remember:** The key to mastering SQL for interviews is consistent practice and understanding the logic behind each query!
