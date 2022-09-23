'use strict';
const areaChart =data =>{
    new Chart(document.querySelector('#areachart'), {
        type: 'line',
        data: {
            labels: ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'],
            datasets: [{
                label: 'New Visits',
                data: [24, 10, 14, 12, 10, 8, 10],
                fill: true,
                tension: 0.4,
                borderColor: 'transparent',
                backgroundColor: '#ffbb554f'
            },
            {
                label: 'Regular Visits',
                data: [0, 6, 12, 10, 8, 12, 15],
                fill: true,
                tension: 0.4,
                borderColor: 'transparent',
                backgroundColor: '#ff778236'
            }
        ]},
        options: {
            responsive: true,
            maintainAspectRation: true, 
            scales:{
                y:{
                    beginAtZero: true
                },
                x:{
                    beginAtZero: true
                },
            }
        }
    })
}

const pieChart =data =>{
    new Chart(document.querySelector('#piechart'),{
        type: 'pie',
        data: {
            labels: ['mobile', 'desktop', 'tv'],
            datasets: [{ 
                data: [24, 26, 10],
                backgroundColor: ['#ffbb55', '#41f1b6', '#ff7782'],
                borderColor: ['white', 'white'],
                borderWidth: 1
            }]
        }
         
    })
}