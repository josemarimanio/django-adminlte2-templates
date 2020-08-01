$(function () {
    'use strict';

    var $actions = $('.actions');
    var $object_tools = $('.object-tools');
    var $result_list = $('#result_list');

    $actions.addClass('form-inline');
    $actions.find('select').addClass('form-control input-sm');
    $actions.find(':submit').addClass('btn btn-default btn-sm');

    $object_tools.find('li a').addClass('btn btn-default btn-sm');

    $result_list.addClass('table table-striped table-bordered table-hover');
});
