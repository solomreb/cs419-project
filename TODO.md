# TODO

* view_table.py
    * I am having a hard time visualizing what to do here.
* Insert Into Table
    * Sames as above: can't visualize this one 
* create_table.py
    * createColumns()
		* Do we want to list the options of Types? Or, are we assuming that the user knows the types available
	* It might be easiest for the databast queries to do it this way:
    	* create the table with just the name first CREATE TABLE table_name
    	* then, create the columns using the ALTER TABLE command each time a column is entered? (http://www.techonthenet.com/sql/tables/alter_table.php)
* constants / constraints
	* Maybe we set a max number of columns?



Queries for Viewing table:

-Get all the column names:
	SELECT `COLUMN_NAME` 
	FROM `INFORMATION_SCHEMA`.`COLUMNS` 
	WHERE `TABLE_SCHEMA`='yourdatabasename' 
    AND `TABLE_NAME`='yourtablename';
-run the query and store into the variable 'rows':
	http://stackoverflow.com/questions/28981770/store-sql-result-in-a-variable-in-python

	results will look like this: [['Bob', '9123 4567'], ['Janet', '8888 8888']]
		-this is a query to return name and phone number