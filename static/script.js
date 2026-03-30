function scanInbox() {
    const btn = document.getElementById('scan-btn');
    const terminal = document.getElementById('scan-results');
    
    btn.innerText = "SCANNING...";
    btn.disabled = true;
    
    terminal.innerHTML = '<div class="terminal-line">> ESTABLISHING_CONNECTION...</div>';
    
    fetch('/scan')
        .then(response => response.json())
        .then(data => {
            terminal.innerHTML = '';
            
            // Staggering simulation
            let delay = 0;
            data.results.forEach((item, index) => {
                setTimeout(() => {
                    const div = document.createElement('div');
                    div.className = 'terminal-line';
                    const [subject, prediction] = item;
                    
                    const statusClass = prediction === "Phishing" ? "line-phishing" : "line-legit";
                    
                    div.innerHTML = `<strong class="${statusClass}">[${prediction}]</strong> ${subject}`;
                    terminal.appendChild(div);
                    
                    // Scroll to bottom
                    const termContainer = document.getElementById('scan-terminal');
                    termContainer.scrollTop = termContainer.scrollHeight;
                    
                    // Re-enable button when done
                    if (index === data.results.length - 1) {
                        setTimeout(() => {
                            btn.innerText = "INITIATE_REMOTE_SCAN";
                            btn.disabled = false;
                            
                            const prompt = document.createElement('div');
                            prompt.className = 'terminal-line';
                            prompt.innerText = '> SCAN_COMPLETE_';
                            terminal.appendChild(prompt);
                            termContainer.scrollTop = termContainer.scrollHeight;
                        }, 500);
                    }
                }, delay);
                
                delay += Math.random() * 300 + 100; // random delay between 100-400ms
            });
            
            // Handle empty results
            if(!data.results || data.results.length === 0) {
                terminal.innerHTML = '<div class="terminal-line">> NO_NEW_PAYLOADS_FOUND_</div>';
                btn.innerText = "INITIATE_REMOTE_SCAN";
                btn.disabled = false;
            }
        })
        .catch(err => {
            terminal.innerHTML = `<div class="terminal-line line-phishing">> ERROR_CONNECTION_FAILED</div>`;
            console.error(err);
            btn.innerText = "INITIATE_REMOTE_SCAN";
            btn.disabled = false;
        });
}