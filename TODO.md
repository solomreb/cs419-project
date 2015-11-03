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
* Circular dependencies that need to be fixed
* constants / constraints
    * Maybe we set a max number of columns?
    * Maybe we don't allow users to edit structure (yet)
        * if we have time, we can add this functionality, but for now it could just be, what you've set up is what you get??
