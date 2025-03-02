// async function generatePlan() {
//     const data = {
//         height: document.getElementById('height').value,
//         weight: document.getElementById('weight').value,
//         age: document.getElementById('age').value,
//         gender: document.getElementById('gender').value,
//         activity_level: document.getElementById('activity_level').value,
//         goals: document.getElementById('goals').value
//     };

//     const resultDiv = document.getElementById('result');
//     resultDiv.innerHTML = '<div class="loading">Generating plan...</div>';

//     try {
//         const response = await fetch('/generate-plan', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify(data)
//         });

//         if (!response.ok) {
//             throw new Error(`HTTP error! status: ${response.status}`);
//         }

//         const result = await response.json();
//         if (result.error) {
//             throw new Error(result.error);
//         }

//         resultDiv.innerHTML = `
//             <h2>Your Personalized Diet Plan</h2>
//             <div class="plan-content">${result.diet_plan.replace(/\n/g, '<br>')}</div>
//         `;
//     } catch (error) {
//         resultDiv.innerHTML = `
//             <div class="error">
//                 Error: ${error.message || 'Failed to generate diet plan'}
//             </div>
//         `;
//     }
// }