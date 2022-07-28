# Intent

### *Overview*
Papua New Guinea, a small Island nation situated north of Australia and borders Indonesia has so many small airports that serve much of the population in remote parts of the country. These small aerodromes, termed airstrips have surfaces that are either gravel or grass covered and are usually built into the side of mountains or in the middle of a rainforest. Survey teams that go out to these places survey them using sheets of paper in which the surveyor fills out manually by hand during the airstrip inspection. The parameters of inspection are:
1.	length, width and slope
2.	airstrip gps location
3.	surface type (gravel, grass, sealed, dirt)
4.	surface condition (wet, dry, flooded, soaked)
5.	visual aids for navigation
6.	obstacle limitation surface

This was rather tedious and papers get smudged or are either blown by wind when not bounded to a clipboard, resulting in a less efficient workflow. These data are then entered into a word file template which results in duplication of work. How can this workflow be made efficient for the surveyor in the field and avoid duplicating this in the office when transferring the data into the database? Can this process be digitized by an application that can work offline and the data stored on a local device?

### *Aim*
This project endeavours to eliminate paper entry of survey data by creating a graphical user interface (GUI) where field data is captured instantly and stored as a csv or excel file which can than be used in other data manipulations for GIS vector file creation.

# The Program
The Airstrip Survey program (see figure attached) is a user-friendly interface that shows 8 variables which guides the user to input airstrip survey data. The program also has three buttons placed at the bottom which are “Add”, “Export to Excel” and “Export to CSV”.  These buttons allow the user to retrieve the data from the program or add to it.

![gui1](https://user-images.githubusercontent.com/73019564/181420313-6e2e40f0-c6eb-4e0a-b5ff-8536e0802ce3.jpg)

### *How does it work?*
The Airstrip Survey program works by collecting data from the input fields and stores it in memory as a list using the “Add” button.  This list can than be retrieved via two buttons, “Export to Excel” or the “Export to CSV” button. As explicitly shown by the button names, the retrieved list can be as an excel or a csv type format and is up to the user to choose what format they desire. The program than notifies the user with a pop-up message dialogue box if the export was successful.

![gui2](https://user-images.githubusercontent.com/73019564/181420806-488c818f-bfc9-4d6a-abd6-bc9f12b3a31a.jpg)

# Motivation for program development
The Airstrip Survey program was developed to target technical personnel in the aviation industry in Papua New Guinea. Airstrip surveyors in the past have been using sheets of printed paper to collect airstrip information and on these survey trips, they are exposed to the natural elements of nature. Sheets of paper would either get smudged, disintegrate under wet weather conditions or get blown away by wind if not bounded well. There was also, the tendency to accrue a clutter of survey papers when multiple airstrips where surveyed, which usually was the case. The old process for these airstrip surveyors was that after each survey trip, these survey sheets would then be transferred manually into excel or csv to build a database of the airstrips in the country and to use that to plot on map.

The benefits of the Airstrip Survey program will improve the performance of surveyors in the field and in the office by eliminating the manual entry and protect the data against the natural elements. It makes it possible to digitize on the go and automate the whole process efficiently. 

### *Program development process*
Earlier version of the program was based on having a list view field where with each text input in the text fields this data would then be displayed. However, after some consideration that design had to be changed mostly because:
•	It was merely displaying the data twice
•	Taking up space in the program window
The current design being minimalist was preferred because:
•	Provided a clear prompt to the user to, directing attention to start the data entry process

Throughout the design and testing phase, it was noticed that the text fields needed to be cleared after every entry as these were being cleared manually, placing the program into jeopardy of being inefficient. To solve this, a clear function was then included to handle this.

Despite the clear function being a great inclusion into the program, there was still some uncertainties relating to whether the data was exported to the computer when the user was satisfied with what they have captured with the Airstrip Survey program. Whenever the export buttons where executed, the user was not assured or informed if the export was successful. Therefore, the inclusion of a pop-up message dialogue box was appropriate.

The flow chart below shows just how the program works.

![gui3](https://user-images.githubusercontent.com/73019564/181421711-9bac21d4-b548-40b0-b478-825a91b929c0.jpg)

### *Successes*
Getting the export functions to actually export as excel and csv file formats was a plus for the program. These functions where essentially what the programs end result or output was going to be. Having that functionality completes the program as otherwise the program development would have to be abandoned.

### *Challenges*
Standout challenges where choosing the right library packages and the dependencies needed to build the program. Also, learning to write the program outside of the course materials was quite challenging as well.  To over come these, materials online and tutorials helped grasp the new concepts.

### *Future Developments*
The Airstrip program is a desktop GUI, its envisioned that a mobile platform can be developed to expand its capabilities. Possible library packages is Kivy and there’s documentation out there online which can be used to guide the development of this mobile application. It will maintain the main purpose of collecting data and writing them to the specified file formats however there will be the inclusion of viewing that online on a map. Having that versatility would add a tremendous upgrade to the Airstrip Survey program and would be the preferred software.
