var checks = d3.select('.Predictor')
var i = 0
var data = []
checks.html('')
d3.csv('../../resources/processed_data.csv').then(d => {
    var conts = d.columns.slice(3)
    conts.forEach(element => {
        checks.append('input').attr('type', 'checkbox').attr('class', `${i}`).attr('name', element)
        checks.append('label').attr('for', element).text(element)
        checks.append('hr')
        data.push(0)
        i += 1
    });
})

var boxes = d3.selectAll('input')._groups
console.log(boxes)

d3.select('#predict_btn').on('click', d => {
    fetch(`http://127.0.0.1:5000/${data}`)
        .then(response => response.text())
        .then(d => d3.select('.results').html(`<h1>${d}!</h1>`));
})
