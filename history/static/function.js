function updateMacros(macrosJSON) {
	let macroData = JSON.parse(macrosJSON); // Parse JSON string

	let tableHTML = `<table class="table table-bordered">
						<thead>
							<tr>
								<th>Phase</th>
								<th>Carb Strategy</th>
								<th>Calories</th>
								<th>Protein (g)</th>
								<th>Fats (g)</th>
								<th>Carbs (g)</th>
							</tr>
						</thead>
						<tbody>`;

	Object.entries(macroData).forEach(([phase, strategies]) => {
		Object.entries(strategies).forEach(([strategy, values], index) => {
			let formattedStrategy = strategy.split('_')
			.map(word => word.charAt(0).toUpperCase() + word.slice(1))
			.join(' ');

			tableHTML += `<tr>
							<td>${index === 0 ? phase.charAt(0).toUpperCase() + phase.slice(1) : ""}</td>
							<td>${formattedStrategy}</td>
							<td>${values.calories}</td>
							<td>${values.protein}</td>
							<td>${values.fats}</td>
							<td>${values.carbs}</td>
						  </tr>`;
		});
	});

	tableHTML += `</tbody></table>`;

	document.getElementById("macrosContent").innerHTML = tableHTML;
}