// App paths
const APP_PATHS = {
    writer: '../HTMLWriter/HTMLWriter v3.0.0.html',
    todo: '../HTMLToDo/HTMLToDo v5.7.0.html',
    kanban: '../HTMLKanban/HTMLKanban v2.0.0.html'
};

// Load the Writer app
async function loadWriter() {
    const response = await fetch(APP_PATHS.writer);
    const html = await response.text();
    injectApp(html, 'writer');
}

// Load the Todo app
async function loadTodo() {
    const response = await fetch(APP_PATHS.todo);
    const html = await response.text();
    injectApp(html, 'todo');
}

// Load the Kanban app
async function loadKanban() {
    const response = await fetch(APP_PATHS.kanban);
    const html = await response.text();
    injectApp(html, 'kanban');
}

// Helper function to inject app content
function injectApp(html, appName) {
    const container = document.getElementById('app-container');
    
    // Create a back button
    const backButton = document.createElement('button');
    backButton.textContent = '← Back to Home';
    backButton.style.position = 'fixed';
    backButton.style.top = '1rem';
    backButton.style.left = '1rem';
    backButton.style.zIndex = '1000';
    backButton.onclick = goHome;
    
    // Parse the HTML
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    
    // Extract styles
    const styles = doc.getElementsByTagName('style');
    const scripts = doc.getElementsByTagName('script');
    
    // Clear container
    container.innerHTML = '';
    
    // Add back button
    container.appendChild(backButton);
    
    // Add styles
    Array.from(styles).forEach(style => {
        container.appendChild(style.cloneNode(true));
    });
    
    // Add main content
    const content = doc.body.innerHTML;
    const contentDiv = document.createElement('div');
    contentDiv.innerHTML = content;
    container.appendChild(contentDiv);
    
    // Add scripts
    Array.from(scripts).forEach(script => {
        const newScript = document.createElement('script');
        if (script.src) {
            newScript.src = script.src;
        } else {
            newScript.textContent = script.textContent;
        }
        container.appendChild(newScript);
    });
} 