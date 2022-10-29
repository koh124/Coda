function HighLight(file_id) {
  this.file_id = file_id;
}

HighLight.prototype.addInputEventHighLight = function() {
  const tab_content = $(`.tab-pane.code.${this.file_id}`);
  const editor = tab_content.find('textarea.editor-code')[0];
  const code = tab_content.find('code.code-output')[0];

  editor.addEventListener('input', function() {
    code.textContent = this.value;
    hljs.initHighlightingOnLoad();

    const self = this;
    const lines = function() { return self.value.split(/\r*\n/); }
    const lineCount = lines().length;

    const activeEditorLines = tab_content.find('.editor-container .editor-lines')[0];

    let elements = '';
    for (let i = 1; i <= lineCount; i++) {
      elements += `<div class="line"><span>${i}</span></div>`;
    }
    activeEditorLines.innerHTML = elements;

    const line_highlight = $('.line-highlight');
    line_highlight.css('top', `calc(23.625px * ${lineCount - 1})`);
  });
}

HighLight.prototype.addFocusEventHighLight = function() {
  const tab_content = $(`.tab-pane.code.${this.file_id}`);
  const editor = tab_content.find('textarea.editor-code')[0];

  // focusイベントでも発火させないと、行数が表示されない
  editor.addEventListener('focus', function() {
    const self = this;
    const lines = function() { return self.value.split(/\r*\n/); }
    const lineCount = lines().length;

    const activeEditorLines = tab_content.find('.editor-container .editor-lines')[0];

    let elements = ''
    for (let i = 1; i <= lineCount; i++) {
      elements += `<div class="line"><span>${i}</span></div>`;
    }
    activeEditorLines.innerHTML = elements;

    const line_highlight = $('.line-highlight');
    line_highlight.css('top', `calc(23.625px * ${lineCount - 1})`);
  });
}
