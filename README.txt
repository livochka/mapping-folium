web_map makes html map with name and location of filming movies in year specified by user
File location.list was prosessed with get_info module and location module, divided by years and saved in '.csv' files.
Coordinates were found due Google API and included in '.csv' files, so you don't need to find coordinates 
each time you use programm.

Includes:
main.py 
get_info.py
get_info_year.py
location_module.py
get_map.py


Programm use:
	main.py:
		The main module.
		get_year() - get year from user
		main() - call get_year(), saves info from varied '.csv' file in variable 'info', 
		 	then call create_map(info) and Map_year.html saves in the directory.

	get_info_year.py:
		Module to read information from year.csv file
		read_location() - read info from year.csv file, return the dictionary with country as key,
				[film, latitude, longitude] as value.
	
	get_map.py:
		Module to design a map.
		create_map() - creates map with special layer for each country.


Module used for divided informaition into year.csv files:

	get_info.py:
		Module to read information from locations.list
		Call read_file(), return dictionary with year as key, list with name of film and location as info.

	location_module.py:
		Get information year by year from get_info, save in .csv file in form:
		film, country, lat, long
		
		
	


	



	