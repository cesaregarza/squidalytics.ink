// Get the version selector and content divs
const versionSelector = document.querySelector('#version-selector');
const versionContents = document.querySelectorAll('.version-content');

// Function to show a version and hide all others
function showVersion(name) {
    versionContents.forEach(content => {
        if (content.id === 'version-' + name) {
            content.style.display = 'block';
        } else {
            content.style.display = 'none';
        }
    });
}

// Attach change event listener to the selector
versionSelector.addEventListener('change', function() {
    showVersion(this.value);
});

// Show the first version by default
if (versionSelector.options.length > 0) {
    showVersion(versionSelector.options[versionSelector.selectedIndex].value);
}
