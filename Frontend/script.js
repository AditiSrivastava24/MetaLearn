let difficulty = "medium"
let correctAnswer = ""

async function loadQuestion() {

    try {

        const response = await fetch(`http://127.0.0.1:8000/question?difficulty=${difficulty}`)
        const data = await response.json()

        console.log("Question data:", data)

        if(!data.question){
            document.getElementById("question").innerText = "Error loading question"
            return
        }

        document.getElementById("question").innerText = data.question

        document.getElementById("optionA").innerText = data.options.A
        document.getElementById("optionB").innerText = data.options.B
        document.getElementById("optionC").innerText = data.options.C
        document.getElementById("optionD").innerText = data.options.D

        correctAnswer = data.correct_answer

        document.getElementById("message").innerText = ""

    } catch(error){

        console.error("Error loading question:", error)
        document.getElementById("question").innerText = "Failed to load question"

    }
}


async function submitAnswer(option){

    let accuracy = 0

    if(option === correctAnswer){
        document.getElementById("message").innerText = "Correct!"
        accuracy = 1
    }
    else{
        document.getElementById("message").innerText = "Wrong!"
        accuracy = 0
    }

    try{

        const response = await fetch("http://127.0.0.1:8000/predict",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body: JSON.stringify({
                accuracy: accuracy,
                time_score: 0.7,
                confidence: 1,
                attempt: 1
            })

        })

        const result = await response.json()

        console.log("Prediction:", result)

        difficulty = result.next_difficulty

        setTimeout(loadQuestion,1000)

    }catch(error){

        console.error("Prediction error:", error)

    }

}

loadQuestion()