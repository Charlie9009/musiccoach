document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('practiceChart');
    if (!canvas) return;

    // Parse JSON safely from Django's json_script
    const chartLabels = JSON.parse(document.getElementById('chart-labels').textContent);
    const chartData = JSON.parse(document.getElementById('chart-data').textContent);

    const ctx = canvas.getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: chartLabels,
            datasets: [{
                label: 'Minutes per Day',
                data: chartData,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1,
                borderRadius: 5
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Minutes'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Day of Week'
                    }
                }
            }
        }
    });
});
