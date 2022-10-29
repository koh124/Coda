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
  // return 'file_new' + String(this.getCountOfNewFileForEachModule(this.module_id));
  return 'file_new' + String(this.getCountOfNewFile());
}
File.prototype.getCountOfNewFile = function() {
  return $(`li.nav-item.new`).length;
}
File.prototype.getCountOfNewFileForEachModule = function(module_id) {
  return $(`li.nav-item.${module_id}.new`).length;
}
File.prototype.createElementNewFileNavItem = function() {
  const module_id = this.module_id;
  // const new_file_count_in_module = this.getCountOfNewFileForEachModule(module_id);
  const new_file_count_in_module = this.getCountOfNewFile();
  return `<li class="nav-item ${module_id} new ${$(`.module-box.show.${module_id}`).length ? '' : 'none'}" role="presentation">
          <button
            class="nav-link new"
            id="file_new${new_file_count_in_module}-tab"
            data-bs-toggle="tab"
            data-bs-target="#file_new${new_file_count_in_module}"
            type="button"
            role="tab"
            aria-controls="file_new${new_file_count_in_module}"
            aria-selected="true"
          >
          <input class="file-name-form" type="text" name="file_new${new_file_count_in_module}-name" value="" placeholder="ファイル名">
          <span>×</span>
          </button>
          </li>`;
}
File.prototype.createElementNewFileTabContent = function() {
  const module_id = this.module_id;
  // const new_file_count_in_module = this.getCountOfNewFileForEachModule();
  const new_file_count_in_module = this.getCountOfNewFile();
  return `<div
  class="${module_id} file_new${new_file_count_in_module} tab-pane fade code"
  id="file_new${new_file_count_in_module}"
  role="tabpanel"
  aria-labelledby="file_new${new_file_count_in_module}-tab"
  >
    <div class="editor-container">
      <div class="editor-lines"></div>
      <div class="editor-main editor-code">
        <textarea class="editor editor-code editor-codefile_new${new_file_count_in_module}" cols="30" rows="30" name="${module_id}file_new${new_file_count_in_module}-code"></textarea>
        <pre><code class="python code-output code-outputfile_new${new_file_count_in_module}"></code></pre>
      </div>
      <div class="line-highlight"></div>
    </div>
  </div>`;
}
