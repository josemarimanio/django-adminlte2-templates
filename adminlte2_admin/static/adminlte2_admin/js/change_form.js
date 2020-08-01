$(function () {
    'use strict';

    var $object_tools = $('.object-tools');
    var $fields = $('.form-row');
    var $submit_row = $('.submit-row');

    $object_tools.find('li a').addClass('btn btn-default btn-sm');

    $fields.addClass('form-group');
    $fields.find('div[class*=field-] input:not([type=checkbox])[id*=id_], div[class*=field-] select[id*=id_]').addClass('form-control');

    $submit_row.find('a.deletelink').addClass('btn btn-danger');
    $submit_row.find(':submit').addClass('btn btn-default');
});
