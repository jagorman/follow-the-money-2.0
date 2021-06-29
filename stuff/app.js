// from data.js

d3.json('./stuff/Kansas.json').then(data => {
    var tableData = data;
    // console.log(data)
    // Creating References to tbody, input and button
    var $tbody = d3.select("tbody");
    var button = d3.select("#filter-btn");
    var inputFieldDate = d3.select("Candidate");
    //var inputFieldCity = d3.select("#city");
    var columns = ["Candidate", "Contributor", "Total"]

    // Inputing the data into the HTML
    var addData = (dataInput) => {
        dataInput.forEach(candidate => {
            try {
                var row = $tbody.append("tr");
                columns.forEach(column => row.append("td").text(candidate[column]))
            } catch (error) {
                console.error(error)
            }
        });
    }
    addData(tableData)
})

function selectCan(candidate) {
    console.log(candidate)
    d3.json('./stuff/Kansas.json').then(data => {
    var tableData = data;
    // console.log(data)
    // Creating References to tbody, input and button
    var $tbody = d3.select("tbody");
    $tbody.html("<tbody></tbody>");
    //var inputFieldCity = d3.select("#city");
    var columns = ["Candidate", "Contributor", "Total"]
    var filteredData = tableData.filter(contributor => {
        return contributor.Candidate == candidate
    });
    
console.log(filteredData)
    // Inputing the data into the HTML
    var addData = (dataInput) => {
        dataInput.forEach(candidate => {
            try {
                var row = $tbody.append("tr");
                columns.forEach(column => row.append("td").text(candidate[column]))
            } catch (error) {
                console.error(error)
            }
        });
    }
    addData(filteredData)
})};
//

// Event Handler Function
// function runEvent(){    
//    // Prevent Page from Refreshing
//   // d3.event.preventDefault(); 
//    // Select the input element and get the raw HTML node

//    var inputElement = d3.select("candidate");

//    // Get the input value (date) from the input element
//    var inputData = inputElement.property("contributor");

//    //Check for input data
//     if (inputData == "") {inputData = tableData[0].candidate;}


//    // Filter the data.js by the input value
//    var filteredData = tableData.filter(contributor => contributor.candidate === inputData);

//    // Call the createTable function with the
//    // filteredData as the parameter

//    createTable(filteredData);

// };

// runEvent();
