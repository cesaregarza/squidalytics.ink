function renderMathInDocument() {
    renderMathInElement(document.body, {
        // custom options
        delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "\\[", right: "\\]", display: true},
            {left: "\\(", right: "\\)", display: false},
        ]
    });
}
