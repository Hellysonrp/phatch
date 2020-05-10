﻿# -*- coding: utf-8 -*-

# Copyright (C) 2009 www.stani.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/

# generated by wxGlade 0.6.3 on Sat Aug 22 16:01:46 2009

# NO PEP 8

if __name__ == '__main__':
    #to run examples
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')
    import gettext
    gettext.install("test")

import operator
import os

import wx
from wx.lib.newevent import NewEvent

from lib import listData
from lib.system import start
from lib.openImage import open_thumb

from compatible import SearchCtrl
from wxPil import pil_wxBitmap

# begin wxGlade: extracode
# end wxGlade

class ListCtrl(wx.ListCtrl):

    def __init__(self, *args, **kwds):
        kwds["style"] = wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_VIRTUAL
        super(ListCtrl, self).__init__(*args, **kwds)

    def CreateColumns(self):
        for col, header in enumerate(self.data.get_headers()):
            self.InsertColumn(col, _(header))

    def InitData(self, data):
        self.data = data
        self.CreateColumns()
        self.RefreshAllItems()

    def SetData(self, data, amount=None):
        if self.data.set_data(data, amount):
            self.RefreshAllItems()

    def SetFilter(self, filter):
        if self.data.set_filter(filter):
            self.RefreshAllItems()

    def RefreshAllItems(self):
        self.SetItemCount(self.data.amount)
        #self.RefreshItems(0, self.data. amount)

    def OnGetItemText(self, item, col):
        return self.data.get(item, col)

    def OnGetItemAttr(self, item):
        return None

    def OnGetItemImage(self, item):
        return -1


class WxgPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: WxgPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.splitter = wx.SplitterWindow(self, -1, style=wx.SP_NOBORDER)
        self.list_panel = wx.Panel(self.splitter, -1)
        self.tree_panel = wx.Panel(self.splitter, -1)
        self.filter = SearchCtrl(self, -1)
        self.tree = wx.TreeCtrl(self.tree_panel, -1, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)
        self.preview = wx.StaticBitmap(self.tree_panel, -1, wx.NullBitmap)
        self.list = ListCtrl(self.list_panel, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: WxgPanel.__set_properties
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        self.filter.SetFocus()
        self.tree.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.preview.SetMinSize((128, 128))
        self.preview.Hide()
        self.tree_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: WxgPanel.__do_layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        tree_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7.Add(self.filter, 1, wx.EXPAND, 0)
        main_sizer.Add(sizer_7, 0, wx.EXPAND, 0)
        tree_sizer.Add(self.tree, 1, wx.EXPAND, 0)
        tree_sizer.Add(self.preview, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 6)
        self.tree_panel.SetSizer(tree_sizer)
        list_sizer.Add(self.list, 1, wx.EXPAND, 0)
        self.list_panel.SetSizer(list_sizer)
        self.splitter.SplitVertically(self.tree_panel, self.list_panel)
        main_sizer.Add(self.splitter, 1, wx.EXPAND, 0)
        self.SetSizer(main_sizer)
        main_sizer.Fit(self)
        # end wxGlade

# end of class WxgPanel

SelectedEvent, EVT_ITEM_SELECTED = NewEvent()
ActivatedEvent, EVT_ITEM_ACTIVATED = NewEvent()


class Panel(WxgPanel):

    def __init__(self, parent, id, data, Data, headers=None, **options):
        WxgPanel.__init__(self, parent, -1, **options)
        self._tree()
        self.SetData(data, Data, headers)
        self._events()

    def _tree(self, root_label=_('all'), icon=wx.ART_FOLDER):
        self.splitter.SetSashPosition(200)
        il = wx.ImageList(16, 16)
        il.Add(wx.ArtProvider.GetBitmap(icon, wx.ART_OTHER, (16, 16)))
        self.tree.AssignImageList(il)
        self.tree.AddRoot(root_label)

    def _events(self):
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_tree_sel_changed)
        self.filter.Bind(wx.EVT_TEXT, self.on_filter_text)

    def SetData(self, data_tree, Data, headers, id='path'):
        root = self.tree.GetRootItem()
        self.tree.CollapseAndReset(root)
        self.data_tree = []
        self._append_children(root, self.tree.GetItemText(root), data_tree)
        if self.data_tree:
            all = reduce(operator.add, self.data_tree)
        else:
            all = []
        self.data_tree.insert(0, all)
        self.tree.SetPyData(root, 0)
        self.tree.ExpandAll()
        self.list.InitData(Data(all,headers=headers, id=id))

    def SetColumnWidths(self, *widths):
        for col, width in enumerate(widths):
            self.list.SetColumnWidth(col, width)

    def UpdateHeaders(self, headers=None):
        data = self.list.data
        data.update_headers(headers)
        for col, header in enumerate(data.get_headers()):
            item = wx.ListItem()
            item.SetText(header)
            self.list.SetColumn(col, item)

    def GetTreeLabel(self, label, parent_label):
        return label

    def _append_children(self, parent, parent_label, data_tree):
        keys = sorted(data_tree.keys())
        for key in keys:
            item = self.tree.AppendItem(parent, self.GetTreeLabel(key, parent_label), 0)
            self.data_tree.append(data_tree[key]['data'])
            self.tree.SetPyData(item, len(self.data_tree))
            self._append_children(item, key, data_tree[key]['children'])

    def on_tree_sel_changed(self, event):
        index = self.tree.GetPyData(event.GetItem())
        self.list.SetData(self.data_tree[index])

    def on_filter_text(self, event):
        self.list.SetFilter(self.filter.GetValue())


class OpenMixin(object):

    def _events(self):
        super(OpenMixin, self)._events()
        self.tree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_tree_item_activated)
        self.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_list_item_activated)

    def get_tree_folder(self, item):
        index = self.tree.GetPyData(item)
        return os.path.split(self.data_tree[index][0]['path'])[0]

    def get_list_file(self, index):
        return self.list.data.get_by_header(index, 'path')

    def start_tree_item(self, item):
        start(self.get_tree_folder(item))

    def start_list_item(self, index):
        start(self.get_list_file(index))

    def on_list_item_activated(self, event):
        self.start_list_item(event.GetIndex())

    def on_tree_item_activated(self, event):
        self.start_tree_item(event.GetItem())

    def GetTreeLabel(self, label, parent_label):
        return label.replace(parent_label,'')

class PreviewMixin(OpenMixin):

    def _events(self):
        self.preview_sizer = self.preview.GetContainingSizer()
        super(PreviewMixin, self)._events()
        self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_list_item_selected)

    def show_preview(self, filename):
        bitmap = pil_wxBitmap(open_thumb(filename, size=(128,128)))
        self.preview.SetBitmap(bitmap)
        size    = (bitmap.GetWidth(), bitmap.GetHeight())
        self.preview.SetSize(size)
        self.preview.SetMinSize(size)
        self.preview.Show()
        self.preview_sizer.Layout()

    def on_list_item_selected(self, event):
        filename = self.get_list_file(event.GetIndex())
        self.show_preview(filename)

def example_data_tuple():
    data = {'folder0': {'children': {},
            'data': [('item00', 'item00'), ('item01', 'item01'), ('item02', 'item02')]},
        'folder1': {'children': {},
            'data': [('item10', 'item10'), ('item11', 'item11')]},
        'folder2': {'children': {'folder3': {'children': {},
                'data': [('item30', 'item30'), ('item31', 'item31')]}},
            'data': [('item20', 'item20'), ('item21', 'item21')]}}
    files = [('f0/i00', 0), ('f0/i01', 1), ('f1/i10', 2), ('f1/f2/i120', 3)]
    data = listData.files_data_tuple(files)
    app = wx.PySimpleApp(0)
    frame = wx.Frame(None, -1, size=(800, 600))
    panel = Panel(frame, -1, data, listData.DataTuple)
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()


def example_dict_data():
    files = [{'path': 'f0/i00', 'name': 'i00', 'size': '5kb'},
        {'path': 'f0/i01', 'name': 'i01', 'size': '1kb'},
        {'path': 'f1/i10', 'name': 'i10', 'size': '2kb'},
        {'path': 'f1/f2/i120', 'name': 'i120', 'size': '3kb'}]
    data = listData.files_data_dict(files)
    app = wx.PySimpleApp(0)
    frame = wx.Frame(None, -1, size=(800, 600))
    FilePanel = type('FilePanel', (OpenMixin,Panel), {})
    panel = FilePanel(frame, -1, data, listData.DataDict)
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    #example_data_tuple()
    example_dict_data()
