Session 1: The Code Box (Variables & Changing Data)
💻 

  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JS Lesson 1: Variables</title>
</head>
<body>

    <h1>JavaScript Lesson 1: Variables & The Console</h1>

<lesson>
<div>
  The Concept
In programming, you need a way to remember data. Think of a Variable as a labeled storage box.

We use let to create a box whose contents can change later (like a score in a game).

We use const to create a box whose contents are locked and can never change (like your name or a fixed setting).
  </div>
  </lesson>


  
    <p>Press <strong>F12</strong> (or Right-Click and choose <strong>Inspect</strong>), then click the <strong>Console</strong> tab to see JavaScript working behind the scenes!</p>

    <button onclick="viewBoxContents()">Show Box Contents</button>
    <button onclick="changeBoxContents()">Change Box Contents</button>

    <script>
        // 1. We create a locked box using 'const' (Cannot be changed later)
        const developerName = "Future JS Master";

        // 2. We create a flexible box using 'let' (Can be changed later)
        let standardScore = 10;

        // This function prints the starting data to your browser console
        function viewBoxContents() {
            console.log("--- Current Box Status ---");
            console.log("Developer Name (const): " + developerName);
            console.log("Current Score (let): " + standardScore);
        }

        // This function modifies the flexible box and shows the result
        function changeBoxContents() {
            console.log("--- Changing Data Now ---");
            
            // We add 5 points to our score box
            standardScore = standardScore + 5; 
            console.log("New Updated Score: " + standardScore);

            // TRY THIS: Uncomment the line below by removing the '//' to see what happens when you try to change a const!
            // developerName = "Someone Else"; 
        }
    </script>

</body>
</html>
