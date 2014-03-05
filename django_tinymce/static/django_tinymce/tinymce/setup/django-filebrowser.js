function DjangoFilebrowser(field_name, url, type, win) {

    'use strict';

    var editor = win.tinyMCE.activeEditor,
        cmsURL = '/admin/filebrowser/browse/?pop=2';
    cmsURL += '&type=' + type;

    editor.windowManager.open({
        'title': 'Django FileBrowser',
        'url': cmsURL,
        'width': 980,
        'height': 500
    }, {
        'window': win,
        'input': field_name,
        'editor_id': editor.editorId
    });
    return false;
}
