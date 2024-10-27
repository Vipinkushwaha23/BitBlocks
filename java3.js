document.addEventListener("DOMContentLoaded", function () {
    const ctx1 = document.getElementById('chart1').getContext('2d');
    const ctx2 = document.getElementById('chart2').getContext('2d');
    const ctx3 = document.getElementById('chart3').getContext('2d');
    const ctx4 = document.getElementById('chart4').getContext('2d');
    const ctx5 = document.getElementById('chart5').getContext('2d');
    const ctx6 = document.getElementById('chart6').getContext('2d');

    // Example Chart Data
    const chartData = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Dataset 1',
            data: [10, 20, 30, 40, 50, 60],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }, {
            label: 'Dataset 2',
            data: [60, 50, 40, 30, 20, 10],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    const chartOptions = {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    };

    new Chart(ctx1, { type: 'line', data: chartData, options: chartOptions });
    new Chart(ctx2, { type: 'bar', data: chartData, options: chartOptions });
    new Chart(ctx3, { type: 'line', data: chartData, options: chartOptions });
    new Chart(ctx4, { type: 'line', data: chartData, options: chartOptions });
    new Chart(ctx5, { type: 'bar', data: chartData, options: chartOptions });
    new Chart(ctx6, { type: 'line', data: chartData, options: chartOptions });
});
