// Game state
let scores = {
    player: 0,
    computer: 0,
    tie: 0
};

// Choice to emoji mapping
const choiceToEmoji = {
    rock: "✊",
    paper: "✋",
    scissors: "✌️"
};

// Create particles
function createParticles() {
    const particlesContainer = document.getElementById('particles');
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        
        // Random position
        const posX = Math.random() * 100;
        const posY = Math.random() * 100;
        
        // Random size
        const size = Math.random() * 3 + 1;
        
        // Random opacity
        const opacity = Math.random() * 0.5 + 0.1;
        
        // Random color
        const colors = ['#00ffff', '#ff00ff', '#ffff00', '#ffffff'];
        const color = colors[Math.floor(Math.random() * colors.length)];
        
        // Set styles
        particle.style.left = `${posX}%`;
        particle.style.top = `${posY}%`;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.opacity = opacity;
        particle.style.backgroundColor = color;
        particle.style.boxShadow = `0 0 ${size * 2}px ${color}`;
        
        // Add animation
        const duration = Math.random() * 50 + 10;
        const delay = Math.random() * 5;
        particle.style.animation = `float ${duration}s ${delay}s linear infinite`;
        
        particlesContainer.appendChild(particle);
    }
}

// Add floating animation
const style = document.createElement('style');
style.innerHTML = `
    @keyframes float {
        0% { transform: translateY(0) translateX(0); }
        25% { transform: translateY(-20px) translateX(10px); }
        50% { transform: translateY(-40px) translateX(0); }
        75% { transform: translateY(-20px) translateX(-10px); }
        100% { transform: translateY(0) translateX(0); }
    }
`;
document.head.appendChild(style);

// Play a round
function play(playerChoice) {
    // Add click effect
    const buttons = document.querySelectorAll('.choice');
    buttons.forEach(btn => {
        btn.style.pointerEvents = 'none';
        setTimeout(() => {
            btn.style.pointerEvents = 'auto';
        }, 1500);
    });

    // Get computer choice
    const choices = ["rock", "paper", "scissors"];
    const computerChoice = choices[Math.floor(Math.random() * choices.length)];
    
    // Determine winner
    let result;
    if (playerChoice === computerChoice) {
        result = "tie";
    } else if (
        (playerChoice === "rock" && computerChoice === "scissors") ||
        (playerChoice === "paper" && computerChoice === "rock") ||
        (playerChoice === "scissors" && computerChoice === "paper")
    ) {
        result = "win";
    } else {
        result = "lose";
    }
    
    // Update scores
    updateScores(result);
    
    // Update display
    updateDisplay(playerChoice, computerChoice, result);

    // Add sound effect
    playSound(result);
}

// Update scores
function updateScores(result) {
    if (result === "win") {
        scores.player++;
        document.getElementById("player-score").textContent = scores.player;
        document.getElementById("player-score").classList.add('win');
        setTimeout(() => {
            document.getElementById("player-score").classList.remove('win');
        }, 1500);
    } else if (result === "lose") {
        scores.computer++;
        document.getElementById("computer-score").textContent = scores.computer;
        document.getElementById("computer-score").classList.add('lose');
        setTimeout(() => {
            document.getElementById("computer-score").classList.remove('lose');
        }, 1500);
    } else {
        scores.tie++;
        document.getElementById("tie-score").textContent = scores.tie;
        document.getElementById("tie-score").classList.add('tie');
        setTimeout(() => {
            document.getElementById("tie-score").classList.remove('tie');
        }, 1500);
    }
}

// Update display
function updateDisplay(playerChoice, computerChoice, result) {
    const playerEmoji = choiceToEmoji[playerChoice];
    const computerEmoji = choiceToEmoji[computerChoice];
    
    let resultText;
    if (result === "win") {
        resultText = `${playerEmoji} x ${computerEmoji}<br><span class="win">You win!</span>`;
    } else if (result === "lose") {
        resultText = `${playerEmoji} x ${computerEmoji}<br><span class="lose">Computer wins!</span>`;
    } else {
        resultText = `${playerEmoji} x ${computerEmoji}<br><span class="tie">tie</span>`;
    }
    
    document.getElementById("result-text").innerHTML = resultText;
}

// Play sound effect
function playSound(result) {
    // Create audio context
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    const audioCtx = new AudioContext();
    
    // Create oscillator
    const oscillator = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();
    
    // Connect nodes
    oscillator.connect(gainNode);
    gainNode.connect(audioCtx.destination);
    
    // Set sound parameters based on result
    if (result === "win") {
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(440, audioCtx.currentTime); // A4
        oscillator.frequency.linearRampToValueAtTime(880, audioCtx.currentTime + 0.2); // A5
        gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.5);
    } else if (result === "lose") {
        oscillator.type = 'sawtooth';
        oscillator.frequency.setValueAtTime(220, audioCtx.currentTime); // A3
        oscillator.frequency.linearRampToValueAtTime(110, audioCtx.currentTime + 0.3); // A2
        gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.5);
    } else { // tie
        oscillator.type = 'triangle';
        oscillator.frequency.setValueAtTime(330, audioCtx.currentTime); // E4
        oscillator.frequency.linearRampToValueAtTime(330, audioCtx.currentTime + 0.3); // Stay the same
        gainNode.gain.setValueAtTime(0.2, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.5);
    }
}

// Initialize particles
document.addEventListener('DOMContentLoaded', createParticles);
