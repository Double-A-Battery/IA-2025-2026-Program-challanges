function calculate() {
    let team1Name = document.getElementById("T1").value;
    let team1Tries = parseInt(document.getElementById("Tries1").value) || 0;
    let team1Conversions = parseInt(document.getElementById("Con1").value) || 0;
    let team1Penalties = parseInt(document.getElementById("pen2").value) || 0;

    let team2Name = document.getElementById("T2").value;
    let team2Tries = parseInt(document.getElementById("Tries2").value) || 0;
    let team2Conversions = parseInt(document.getElementById("Con2").value) || 0;
    let team2Penalties = parseInt(document.getElementById("Pen2").value) || 0;

    // Calculating total points (assuming 5 points for a try, 2 for a conversion, and 3 for a penalty)
    let team1Points = (team1Tries * 5) + (team1Conversions * 2) + (team1Penalties * 3);
    let team2Points = (team2Tries * 5) + (team2Conversions * 2) + (team2Penalties * 3);

    // Displaying the result
    let resultText = `${team1Name} scored ${team1Points} points. ${team2Name} scored ${team2Points} points.`;
    document.getElementById("result").innerText = resultText;
}