// from data.js
var tableData = data;

// Creating References to tbody, input and button
var $tbody = d3.select("tbody");
var button = d3.select("#filter-btn");
var inputFieldDate = d3.select("Candidate");
//var inputFieldCity = d3.select("#city");
var columns = ["Name", "Office", "Party", "Total Donations", "Top Donor", "Top Company Donor", "Comments"]

// Inputing the data into the HTML
var addData = (dataInput) => {
    dataInput.forEach(candidate => {
        var row = $tbody.append("tr");
        columns.forEach(column => row.append("td").text(candidate[column])
        )
   });
}

addData(tableData)

// Event Handler Function
function runEvent(){
   // Prevent Page from Refreshing
   //d3.event.preventDefault();
   // Select the input element and get the raw HTML node

   var inputElement = d3.select("candidate");

   // Get the input value (date) from the input element
   var inputData = inputElement.property("donor");

   //Check for input data
       if (inputData == "") {inputData = tableData[0].candidate;}


   // Filter the data.js by the input value
   var filteredData = tableData.filter(donor => donor.candidate === inputData);

   // Call the createTable function with the
   // filteredData as the parameter

   createTable(filteredData);

};

runEvent();
