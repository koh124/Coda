const LANGUAGES = ['python', 'Python', 'php', 'PHP', 'ruby', 'Ruby', 'javascript', 'css', 'html'];
const CSRF_TOKEN = document.getElementsByName('csrfmiddlewaretoken')[0].value;

const getTextAreaLineCount = function(value) {
  return value.split(/\r*\n/).length;
}

const highLightLine = function(value) {
  $('.line-highlight').css('top', `calc(23.625px * ${getTextAreaLineCount(value) - 1})`);
}

const sendAjaxRequest = function(url, method, data, success, failed) {
  $.ajax(url, {
    type: method,
    data: data,
    dataType: 'xml'
  }).done(function(result) {
    success()
  }).fail(function(result) {
    failed()
  })
}

const getActiveFileId = () => getActiveFileTab().attr('id');
const getActiveFileTab = () => $('.tab-pane.code.show.active');
const getActiveCodeTag = () => getActiveFileTab().find('code.code-output')[0];
