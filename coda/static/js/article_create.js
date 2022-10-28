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

// デフォルト引数は普通に使えるが、
// キーワード引数は仮引数も実引数もオブジェクトリテラルで受け渡ししないとだめ
function Module({id, name, is_active, is_new}) {
  this.id        =        id === undefined ? this.getNewModuleId() : id;
  this.name      =      name === undefined ? '' : name;
  this.is_active = is_active === undefined ? false : is_active;
  this.is_new    =    is_new === undefined ? true : is_new;
  Object.freeze(this);
}

// Javascriptのprototypeに保存するメソッドは
// アロー関数だとthisがwindowになって、
// function(){}で定義するとオブジェクトになる やばい
Module.prototype.exists = function(module_id=this.id) {
  return $(`.module-box.${module_id}`).length;
}
Module.prototype.getActiveModuleId = () => $('.module-box.show').attr('id');
Module.prototype.getNewModuleBoxCount = () => $('.module-box.new').length;
Module.prototype.getNewModuleId = function() {
  return 'module_new' + String(this.getNewModuleBoxCount());
}
Module.prototype.createElementNewModule = function() {
  return `<div id="${this.id}" class="${this.id} module-box new show">
            <div class="module-name-box">
              <div class="${this.id} module-name">
                <input id="${this.id}-name-form" type="text" class="${this.id} module-name-form" name="${this.id}-name" value="" placeholder="モジュール名">
              </div>
              <div class="module-name-edit">
                <label for="${this.id}-name-form">
                  <span><i class="fa-solid fa-pen"></i></span>
                </label>
              </div>
            </div>
          </div>`;
}
Module.prototype.addClickEventActivateModule = function() {
  if (this.exists()) {
    const self = this;
    const module = $(`.module-box.${this.id}`).get()[0];

    module.addEventListener('click', function() {
      self.showModule()
      self.activateNavItems();
      self.disableNavItems();
      self.activateTabContent();
      self.disableTabContent();
    });
  } else {
    throw new Error('モジュールが存在しません');
  }
}
Module.prototype.showModule = function() {
  $(this).addClass('show');
  $('.module-box').not(`.${this.id}`).removeClass('show');
}
Module.prototype.activateNavItems = function() {
  /*
  モジュールのクリックイベントで発火したモジュールに属するファイルタブ（nav-item）をactiveにする
  */
  const active_nav_items = $(`li.nav-item.${this.id}`); //同一のモジュールIDを持つタブすべてを一旦disableにする
  for (let i = 0; i < active_nav_items.length; i++) {
    $(active_nav_items[i]).removeClass('none');
    $(active_nav_items[i]).find('button.nav-link.active').removeClass('active');
  }
  $(active_nav_items[0]).find('button.nav-link').addClass('active');
}
Module.prototype.disableNavItems = function() {
  /*
  モジュールのクリックイベントで発火したモジュール以外の
  他のモジュールのファイルタブをすべてnoneにする（表示しない）
  */
  const non_active_nav_items = $('li.nav-item').not(`.${this.id}`).not('#input-nav-item').not('#output-nav-item');
  for (let i = 0; i < non_active_nav_items.length; i++) {
    $(non_active_nav_items[i]).addClass('none');
    $(non_active_nav_items[i]).find('button.nav-link.active').not('#input-tab').not('#output-tab').removeClass('active');
  }
}
Module.prototype.activateTabContent = function() {
  // const visible_tab_contents = $(`.tab-pane.code.file_new${count_new_file}`); //同一のmoduleIDでは？
  const visible_tab_contents = $(`.tab-pane.code.${this.id}`);
  for (let i = 0; i < visible_tab_contents.length; i++) {
    $(visible_tab_contents[i]).removeClass('none');
  }
  $('.tab-pane.code.active.show').removeClass('active show');
  $(visible_tab_contents[0]).addClass('active show');
}
Module.prototype.disableTabContent = function() {
  const non_visible_tab_contents = $('.tab-pane.code').not(`.${this.id}`);
  for (let i = 0; i < non_visible_tab_contents.length; i++) {
    $(non_visible_tab_contents[i]).addClass('none');
  }
}

// 流れ
// モジュールクリック
// アクティブなファイルタブをnoneにし、クリックしたモジュールをshowにする
// それ以外のモジュールのshowは外す
// 一番左のタブのbuttonをactiveにし、モジュールIDが違うタブはすべてnoneにする
// 同じモジュールだが非activeなタブはnoneにもactiveにもしない
// タブのコンテンツからactiveとshowを外す
// 表示するタブコンテンツは今activeなファイルタブに対応するファイルIDを持つコンテンツだけなので、
// 該当のコンテンツだけactive showにする（このとき当初の設定では一番左のファイルを表示するようにしている）
// 表示するべきモジュールIDを持つファイルからすべてnoneを外す
// 違うモジュールIDを持つファイルをすべてnoneにする
