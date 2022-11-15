// フロー
// コンストラクタ起動
// this.getNewFileId() → 新しいファイルIDを生成したい
// <getnewfileid>
// → このファイルが属することになるモジュールにいくつnewファイルがあるか調べたい
// → getCountOfNewFileForEachModule() 呼び出し
// <getCountOfNewFileForEachModule>
// →このファイルが属するモジュールIDを調べる
// →getthismoduleid()呼び出し
// <getThisModuleId>
// →this.idを参照しているためエラー

// 新しいファイルIDの生成ロジック
// このモジュールの中のファイルのnewのlengthで決める
// 'このモジュール'とはなにか。ファイルIDはまだ決定してないため、ファイルIDから逆算することはできない
// 'show'であるモジュールから取得すると、showではない状態でファイルを生成したときに引っかかる
// 新しいモジュールを生成したときに新規ファイルを作成するが、
// その時点では元々選択していたモジュールがshowになっているため、この場合が該当する
// ☆解決
// Fileを作成した時点でコンストラクタにモジュールIDを渡す

function File({id, module_id}) {
  this.module_id = module_id;
  this.id        =        id === undefined ? this.getNewFileId() : id;
}
File.prototype.getThisModuleId = function() {
  // ※ファイルをappendする前だと使えないので注意
  const classes = $(`#${this.id}`)[0].classList;
  for (let i = 0; i < classes.length; i++) {
    if(classes[i].indexOf('module') !== -1) return classes[i];
  }
}
File.prototype.getActiveModuleId = function() {
  return $('.module-box.show').attr('id');
}
File.prototype.getNewFileId = function() {
  // return 'filenew' + String(this.getCountOfNewFileForEachModule(this.module_id));

  let num = this.getCountOfNewFile();
  let file_id = 'filenew' + String(num);
  // newなファイルidの重複があり続ける限り、idをプラス1する
  while ($('.' + file_id).length) {
    num++;
    file_id = 'filenew' + String(num);
  }
  console.log(file_id);
  return file_id;

  return 'filenew' + String(this.getCountOfNewFile());
}
File.prototype.getCountOfNewFile = function() {
  return $(`li.nav-item.new`).length;
}
File.prototype.getCountOfNewFileForEachModule = function(module_id) {
  return $(`li.nav-item.${module_id}.new`).length;
}
File.prototype.createElementNewFileNavItem = function() {
  console.log(this.id, 'これはcreateElementNavitem')
  const module_id = this.module_id;
  // const new_file_count_in_module = this.getCountOfNewFileForEachModule(module_id);
  const new_file_count_in_module = this.getCountOfNewFile();
  // ソース filenew${new_file_count_in_module}
  return `<li class="nav-item ${module_id} new ${$(`.module-box.show.${module_id}`).length ? '' : 'none'}" role="presentation">
          <button
            class="nav-link new"
            id="${this.id}-tab"
            data-bs-toggle="tab"
            data-bs-target="#${this.id}"
            type="button"
            role="tab"
            aria-controls="${this.id}"
            aria-selected="true"
          >
          <input type="hidden" name="${module_id}_${this.id}-id" value="">
          <input class="file-name-form" type="text" name="${module_id}_${this.id}-name" value="" placeholder="ファイル名">
          <span>×</span>
          </button>
          </li>`;
}
File.prototype.createElementNewFileTabContent = function() {
  console.log(this.id, 'これはcreateElement')
  const module_id = this.module_id;
  // const new_file_count_in_module = this.getCountOfNewFileForEachModule();
  const new_file_count_in_module = this.getCountOfNewFile();
  return `<div
  class="${module_id} ${this.id} tab-pane fade code"
  id="${this.id}"
  role="tabpanel"
  aria-labelledby="${this.id}-tab"
  >
    <div class="editor-container">
      <div class="editor-lines"></div>
      <div class="editor-main editor-code">
        <textarea class="editor editor-code editor-code${this.id}" cols="30" rows="30" name="${module_id}_${this.id}-code"></textarea>
        <pre><code class="python code-output code-output${this.id} language-python"></code></pre>
      </div>
      <div class="line-highlight"></div>
    </div>
  </div>`;
}
File.prototype.setDropDownMenuLanguage = function() {
  const file_id = this.id;
  const this_class_list = $(`.tab-pane#${file_id} .editor-container pre code`).get()[0].classList;
  for (let i = 0; i < this_class_list.length; i++) {
    if (LANGUAGES.includes(this_class_list[i]) || LANGUAGES.includes(this_class_list[i].replace('language-', ''))) {
      $('#language-dropdownmenu-button').val(this_class_list[i].replace('language-', ''));
      // $('#language-dropdownmenu-button').val('aaa');
    }
  }
}
File.prototype.exists = function() {
  return $(`.tab-pane.code.${this.id}`).length;
}
