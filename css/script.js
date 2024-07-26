document.addEventListener("DOMContentLoaded", () => {
    let value = localStorage.getItem("coinValue") ? parseInt(localStorage.getItem("coinValue")) : 0;
    let currentImage = localStorage.getItem("coinImage") || './image/level-1.png';

    const coinValueElement = document.getElementById("coin-balance");
    const coinButton = document.getElementById("coin-button");
    const coinImage = document.getElementById("coin-image");

    // Function to increase coin value
    function increaseCoinValue() {
        value++;
        coinValueElement.textContent = value;
        localStorage.setItem("coinValue", value);
        animateCoin();
        updateCoinImage();
    }

    // Function to update coin image based on value
    function updateCoinImage() {
        let newImage;
        if (value >= 700) {
            newImage = './image/level-5.png';
        } else if (value >= 500) {
            newImage = './image/level-4.png';
        } else if (value >= 350) {
            newImage = './image/level-3.png';
        } else if (value >= 200) {
            newImage = './image/level-2.png';
        } else {
            newImage = './image/level-1.png';
        }

        if (newImage !== currentImage) {
            currentImage = newImage;
            coinImage.src = currentImage;
            localStorage.setItem("coinImage", currentImage);
        }
    }

    // Function to animate coin button
    function animateCoin() {
        coinButton.classList.add("shake");
        setTimeout(() => {
            coinButton.classList.remove("shake");
        }, 200);
    }

    // Event listener for coin button
    coinButton.addEventListener("click", increaseCoinValue);

    // Initialize coin value and image on page load
    coinValueElement.textContent = value;
    coinImage.src = currentImage;

    // Debugging: Log current image path
    console.log("Current Image on Load:", currentImage);

    coinImage.onload = () => {
        console.log("Image loaded successfully:", currentImage);
    };

    coinImage.onerror = () => {
        console.error("Image failed to load:", currentImage);
        coinImage.src = './image/level-1.png';
    };
});
