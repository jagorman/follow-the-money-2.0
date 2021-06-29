// from data.js

d3.json('./stuff/Missouri.json').then(data => {
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
    d3.json('./stuff/Missouri.json').then(data => {
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