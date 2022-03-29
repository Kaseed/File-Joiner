The program is used to join two csv files using a specified column, then it writes the result to a standard output. 

Program consists of a join.py file in `src` folder. The program is started with "join.py first_file_path second_file_path column join_type" command 
* __first_file_path__ - path to the first merged csv file
* __second_file_path__ - path to the second merged csv file
* __column__ - header of a column to merge in each file
* __join_type__ - one of the three defined types of join
    * __left__ - left join
    * __right__ - right join
    * __inner__ - inner join
    
Firstly program validates entered arguments and executes one of the three join operations. Left join and right join are the same operation with a different order of arguments. Inner join uses the left join function and deletes rows with added None type cells.