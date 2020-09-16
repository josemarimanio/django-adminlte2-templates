$(function () {
    'use strict';

    var $breadcrumbs = $('.breadcrumbs');
    var divider = '›';

    var $object_tools = $('.object-tools');
    var $fields = $('.form-row');
    var $submit_row = $('.submit-row');

    /*
        Convert default Django Admin breadcrumbs to AdminLTE2 version
                                                                        */
    if ($breadcrumbs.length) {

        var items = $breadcrumbs.html().split(divider);
        var content = '';

        $.each(items, function (index) {
            content += '<li>' + this.toString() + '</li>';
        });

        $breadcrumbs.replaceWith(content);
    }

    /*
       Apply Bootstrap to object tool links
                                                     */
    if ($object_tools.length) {
        $object_tools.find('li a').addClass('btn btn-default btn-sm');
    }

    /*
        Apply Bootstrap to form field elements
                                                        */
    if ($fields.length) {
        $fields.addClass('form-group');
        $fields.find(
            'input:not([type=checkbox])[id*=id_], select[id*=id_]'
        ).addClass('form-control');
    }

    /*
        Apply Bootstrap to submit and delete buttons
                                                            */
    if ($submit_row.length) {
        $submit_row.find('a.deletelink').addClass('btn btn-danger');
        $submit_row.find(':submit').addClass('btn btn-default');
    }
});
