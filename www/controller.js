// Display voice text

const displayBox = document.getElementById("chat-text");

eel.expose(DisplayMessage);
function DisplayMessage(text) {
    displayBox.innerText = text;
    eel.speak(text);
}

// Display start page
eel.expose(ShowHood);
function ShowHood() {
    const startPage = document.getElementById("start-page");
    const voicePage = document.getElementById("voice-page");

    startPage.hidden = false;
    voicePage.hidden = true;
}