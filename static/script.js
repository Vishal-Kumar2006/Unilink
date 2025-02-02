document.addEventListener('DOMContentLoaded', function () {

    let translatedText = ""; // Store translated text for voice to play
    const micIcon = document.getElementById('micIcon'); // Get mic icon element

    // Function to handle Text-to-Text translation
    async function translateText() {
        let text = document.getElementById('sourceText').value.trim();
        let sourceLang = document.getElementById('sourceLanguage').value;
        let targetLang = document.getElementById('targetLanguage').value;

        if (!text) {
            alert("Please enter text to translate!");
            return;
        }

        try {
            let res = await fetch('/translate_text', {
                method: 'POST',
                body: new URLSearchParams({
                    text: text,
                    target_language: targetLang
                }),
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
            });

            let data = await res.json();
            translatedText = data.translated; // Store the translated text
            document.getElementById('translatedText').value = translatedText;

            // Auto-play the translated text
            playVoice(translatedText, targetLang);
        } catch (error) {
            console.error("Translation error:", error);
            alert("Translation failed.");
        }
    }

    // Function to handle Text-to-Voice translation
    async function playVoice(text, language) {
        if (!text) {
            alert("No text available to play.");
            return;
        }

        try {
            let res = await fetch('/generate_speech', {
                method: 'POST',
                body: new URLSearchParams({ text: text, language: language }),
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
            });

            let data = await res.json();
            console.log("Speech generated:", data.message);
        } catch (error) {
            console.error("TTS error:", error);
            alert("Error playing audio.");
        }
    }

    // Function to handle Voice-to-Text translation
    async function voiceToText() {
        let targetLang = document.getElementById('targetLanguage').value;

        // Show microphone icon while listening
        micIcon.style.display = 'block';

        try {
            let res = await fetch('/translate_voice', {
                method: 'POST',
                body: new URLSearchParams({ target_language: targetLang }),
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
            });

            let data = await res.json();
            document.getElementById('sourceText').value = data.translated;
            playVoice(data.translated, targetLang);
        } catch (error) {
            console.error("Voice-to-Text error:", error);
            alert("Error processing voice input.");
        } finally {
            // Hide microphone icon after processing
            setTimeout(() => {
                micIcon.style.display = 'none';
            }, 1000);
        }
    }

    // Function to handle Voice-to-Voice translation
    async function voiceToVoice() {
        let targetLang = document.getElementById('targetLanguage').value;

        // Show microphone icon while listening
        micIcon.style.display = 'block';

        try {
            let res = await fetch('/translate_voice', {
                method: 'POST',
                body: new URLSearchParams({ target_language: targetLang }),
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
            });

            let data = await res.json();
            playVoice(data.translated, targetLang);
        } catch (error) {
            console.error("Voice-to-Voice error:", error);
            alert("Error processing voice input.");
        } finally {
            // Hide microphone icon after processing
            setTimeout(() => {
                micIcon.style.display = 'none';
            }, 1000);
        }
    }

    // Event Listeners for Button Clicks
    document.getElementById('texttotextButton').addEventListener('click', translateText);
    
    document.getElementById('textToVoiceButton').addEventListener('click', () => {
        if (translatedText) {
            let language = document.getElementById('targetLanguage').value;
            playVoice(translatedText, language);
        } else {
            alert("Please translate text first.");
        }
    });

    document.getElementById('voiceToTextButton').addEventListener('click', voiceToText);
    document.getElementById('voiceToVoiceButton').addEventListener('click', voiceToVoice);

});