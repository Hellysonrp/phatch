﻿# -*- coding: utf-8 -*-

# generated by wxGlade 0.5.1cvs on Thu Jun 14 14:07:44 2007 from /home/stani/sync/python/convert/trunk/gui/wxGlade/dialogs.wxg

import wx
from lib.pyWx import folderFileBrowser as ffb
from lib.desktop import USER_FOLDER

class StatusDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: StatusDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.message = wx.StaticText(self.panel_1, -1, _("Done"))
        self.log = wx.Button(self.panel_1, -1, _("Show &Log"))
        self.report = wx.Button(self.panel_1, -1, _("Show &Images"))
        self.ok = wx.Button(self.panel_1, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_button_log, self.log)
        self.Bind(wx.EVT_BUTTON, self.on_button_report, self.report)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: StatusDialog.__set_properties
        self.SetTitle(_("Ready!"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: StatusDialog.__do_layout
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19.Add(self.message, 1, wx.ALL|wx.EXPAND, 6)
        sizer_20.Add(self.log, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_20.Add(self.report, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_20.Add(self.ok, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_19.Add(sizer_20, 0, wx.ALIGN_RIGHT, 0)
        self.panel_1.SetSizer(sizer_19)
        sizer_18.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_18)
        sizer_18.Fit(self)
        self.Layout()
        # end wxGlade

    def on_button_report(self, event): # wxGlade: StatusDialog.<event_handler>
        print "Event handler `on_button_report' not implemented!"
        event.Skip()

    def on_button_log(self, event): # wxGlade: StatusDialog.<event_handler>
        print "Event handler `on_button_log' not implemented!"
        event.Skip()

# end of class StatusDialog


class FolderFileBrowser(ffb.PreviewMixin, ffb.Panel):
    def GetTreeLabel(self, label, parent_label):
        return label[:-1].replace(parent_label,'')\
            .replace(USER_FOLDER,'~')

class ImageTreeDialog(wx.Dialog):
    def __init__(self, data, Data, headers, *args, **kwds):
        # begin wxGlade: ImageTreeDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.MAXIMIZE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, -1)
        self.browser = FolderFileBrowser(self.panel, -1, data, Data, headers)
        self.hint = wx.StaticText(self.panel, -1, _("Double click to open or right click for more options."))
        self.cancel = wx.Button(self.panel, wx.ID_CANCEL, "")
        self.ok = wx.Button(self.panel, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ImageTreeDialog.__set_properties
        self.SetTitle(_("Explorer"))
        self.browser.SetFocus()
        self.hint.Enable(False)
        self.ok.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ImageTreeDialog.__do_layout
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15.Add(self.browser, 1, wx.EXPAND, 0)
        sizer_16.Add(self.hint, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_16.Add(self.cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_16.Add(self.ok, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_15.Add(sizer_16, 0, wx.EXPAND, 0)
        self.panel.SetSizer(sizer_15)
        sizer_14.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_14)
        sizer_14.Fit(self)
        self.Layout()
        # end wxGlade

# end of class ImageTreeDialog


class WritePluginDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: WritePluginDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.icon = wx.StaticBitmap(self, -1, wx.NullBitmap)
        self.message = wx.StaticText(self, -1, _("You only need to know PIL to write a plugin for Phatch,"))
        self.template = wx.CheckBox(self, -1, _("&Show template for action plugin"))
        self.path = wx.StaticText(self, -1, _("Path"))
        self.code = wx.TextCtrl(self, -1, _("Code"), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.help = wx.Button(self, -1, _("&Ask for Help"))
        self.ok_copy_1 = wx.Button(self, wx.ID_OK, _("&OK"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_CHECKBOX, self.on_template, self.template)
        self.Bind(wx.EVT_BUTTON, self.on_help, self.help)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: WritePluginDialog.__set_properties
        self.SetTitle(_("Write Action Plugin"))
        self.icon.SetMinSize((32, 32))
        self.code.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: WritePluginDialog.__do_layout
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9.Add(self.icon, 0, wx.ALL, 6)
        sizer_11.Add(self.message, 0, wx.ALL, 6)
        sizer_11.Add(self.template, 0, wx.ALL, 6)
        sizer_11.Add(self.path, 0, wx.ALL, 6)
        sizer_11.Add(self.code, 1, wx.ALL|wx.EXPAND, 6)
        sizer_10.Add(self.help, 0, wx.ALL|wx.EXPAND, 6)
        sizer_10.Add(self.ok_copy_1, 0, wx.ALL|wx.EXPAND, 6)
        sizer_11.Add(sizer_10, 0, wx.ALIGN_RIGHT, 0)
        sizer_9.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_7.Add(sizer_9, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_7)
        sizer_7.Fit(self)
        self.Layout()
        # end wxGlade

    def on_help(self, event): # wxGlade: WritePluginDialog.<event_handler>
        print "Event handler `on_help' not implemented!"
        event.Skip()

    def on_template(self, event): # wxGlade: WritePluginDialog.<event_handler>
        print "Event handler `on_template' not implemented"
        event.Skip()

# end of class WritePluginDialog


class ErrorDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ErrorDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.icon = wx.StaticBitmap(self, -1, wx.NullBitmap)
        self.message = wx.StaticText(self, -1, "")
        self.future_errors = wx.CheckBox(self, -1, _("Apply for future errors        "))
        self.abort = wx.Button(self, wx.ID_ABORT, _("&Abort"))
        self.ignore = wx.Button(self, wx.ID_IGNORE, _("&Skip to Next Action"))
        self.skip = wx.Button(self, wx.ID_FORWARD, _("Skip To Next &Image"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_abort, id=wx.ID_ABORT)
        self.Bind(wx.EVT_BUTTON, self.on_ignore, id=wx.ID_IGNORE)
        self.Bind(wx.EVT_BUTTON, self.on_skip, id=wx.ID_FORWARD)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ErrorDialog.__set_properties
        self.icon.SetMinSize((32, 32))
        self.ignore.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ErrorDialog.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(self.icon, 0, wx.ALL, 6)
        sizer_2.Add(self.message, 0, wx.ALL, 6)
        sizer_5.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer.Add(sizer_5, 0, wx.EXPAND, 0)
        sizer_4.Add(self.future_errors, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_4.Add(self.abort, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_4.Add(self.ignore, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_4.Add(self.skip, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 6)
        sizer.Add(sizer_4, 0, wx.EXPAND, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

    def on_abort(self, event): # wxGlade: ErrorDialog.<event_handler>
        print "Event handler `on_abort' not implemented!"
        event.Skip()

    def on_skip(self, event): # wxGlade: ErrorDialog.<event_handler>
        print "Event handler `on_skip' not implemented!"
        event.Skip()

    def on_ignore(self, event): # wxGlade: ErrorDialog.<event_handler>
        print "Event handler `on_ignore' not implemented!"
        event.Skip()

    def on_details(self, event): # wxGlade: ErrorDialog.<event_handler>
        print "Event handler `on_details' not implemented"
        event.Skip()

# end of class ErrorDialog


class FilesDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FilesDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.MAXIMIZE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        self.icon = wx.StaticBitmap(self, -1, wx.NullBitmap)
        self.message = wx.StaticText(self, -1, _("Message"))
        self.list = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.cancel = wx.Button(self, wx.ID_CANCEL, _("&Abort"))
        self.ok = wx.Button(self, wx.ID_OK, _("&Continue Anyway"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FilesDialog.__set_properties
        self.icon.SetMinSize((32, 32))
        self.ok.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FilesDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.icon, 0, wx.ALL, 6)
        sizer_12.Add(self.message, 0, wx.ALL, 6)
        sizer_12.Add(self.list, 1, wx.ALL|wx.EXPAND, 6)
        sizer_13.Add(self.cancel, 0, wx.ALL|wx.EXPAND, 6)
        sizer_13.Add(self.ok, 0, wx.ALL|wx.EXPAND, 6)
        sizer_12.Add(sizer_13, 0, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(sizer_12, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class FilesDialog

class ExecuteDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ExecuteDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.sizer_11_copy_4_staticbox = wx.StaticBox(self, -1, _("Options"))
        self.sizer_8_staticbox = wx.StaticBox(self, -1, _("Types"))
        self.browse = wx.Button(self, -1, _("Browse Folder"))
        self.path = wx.TextCtrl(self, -1, "", style=wx.TE_RICH2)
        self.extensions = wx.CheckListBox(self, -1)
        self.source = wx.RadioBox(self, -1, _("Source"), choices=[_("Folder"), _("File(s)"), _("Clipboard")], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.stop_for_errors = wx.CheckBox(self, -1, _("Stop for errors"))
        self.check_images_first = wx.CheckBox(self, -1, _("Check images first"))
        self.overwrite_existing_images = wx.CheckBox(self, -1, _("Overwrite existing images"))
        self.recursive = wx.CheckBox(self, -1, _("Include all subfolders"))
        self.always_show_status_dialog = wx.CheckBox(self, -1, _("Always show status dialog when done"))
        self.desktop = wx.CheckBox(self, -1, _("Always save on desktop"))
        self.repeat_label = wx.StaticText(self, -1, _("Repeat images"))
        self.repeat = wx.SpinCtrl(self, -1, "1", min=1, max=9999999)
        self.select = wx.Button(self, wx.ID_DEFAULT, _("&All Types"))
        self.button_1 = wx.Button(self, wx.ID_CANCEL, _("&Cancel"))
        self.ok_copy = wx.Button(self, wx.ID_OK, _("&Batch"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_browse, self.browse)
        self.Bind(wx.EVT_RADIOBOX, self.on_source, self.source)
        self.Bind(wx.EVT_BUTTON, self.on_default, id=wx.ID_DEFAULT)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ExecuteDialog.__set_properties
        self.source.SetSelection(0)
        self.stop_for_errors.SetValue(1)
        self.check_images_first.SetValue(1)
        self.always_show_status_dialog.SetValue(1)
        self.ok_copy.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ExecuteDialog.__do_layout
        grid_sizer = wx.FlexGridSizer(5, 2, 4, 4)
        sizer_10_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_11_copy_4 = wx.StaticBoxSizer(self.sizer_11_copy_4_staticbox, wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(1, 2, 6, 6)
        sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.VERTICAL)
        grid_sizer.Add(self.browse, 0, wx.ALL|wx.EXPAND, 6)
        grid_sizer.Add(self.path, 1, wx.ALL|wx.EXPAND, 6)
        sizer_8.Add(self.extensions, 1, wx.ALL|wx.EXPAND, 6)
        grid_sizer.Add(sizer_8, 1, wx.ALL|wx.EXPAND, 6)
        sizer_10_copy.Add(self.source, 0, wx.ALL|wx.EXPAND, 6)
        sizer_11_copy_4.Add(self.stop_for_errors, 0, wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_11_copy_4.Add(self.check_images_first, 0, 0, 6)
        sizer_11_copy_4.Add(self.overwrite_existing_images, 0, 0, 6)
        sizer_11_copy_4.Add(self.recursive, 0, wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_11_copy_4.Add(self.always_show_status_dialog, 0, 0, 0)
        sizer_11_copy_4.Add(self.desktop, 0, 0, 0)
        grid_sizer_1.Add(self.repeat_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.repeat, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11_copy_4.Add(grid_sizer_1, 1, 0, 0)
        sizer_10_copy.Add(sizer_11_copy_4, 0, wx.ALL|wx.EXPAND, 6)
        sizer_10_copy.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_10_copy.Add(sizer_6, 0, wx.EXPAND, 0)
        sizer_3.Add(self.select, 0, wx.ALL|wx.EXPAND, 6)
        sizer_3.Add((148, 10), 1, wx.EXPAND, 0)
        sizer_3.Add(self.button_1, 0, wx.ALL|wx.ALIGN_BOTTOM, 6)
        sizer_3.Add(self.ok_copy, 0, wx.ALL|wx.ALIGN_BOTTOM, 6)
        sizer_10_copy.Add(sizer_3, 0, wx.EXPAND, 0)
        grid_sizer.Add(sizer_10_copy, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer)
        grid_sizer.Fit(self)
        grid_sizer.AddGrowableRow(1)
        grid_sizer.AddGrowableCol(1)
        self.Layout()
        # end wxGlade
        self.options_sizer = sizer_11_copy_4

    def on_browse(self, event): # wxGlade: ExecuteDialog.<event_handler>
        print "Event handler `on_browse' not implemented!"
        event.Skip()

    def on_source(self, event): # wxGlade: ExecuteDialog.<event_handler>
        print "Event handler `on_source' not implemented!"
        event.Skip()

    def on_default(self, event): # wxGlade: ExecuteDialog.<event_handler>
        print "Event handler `on_default' not implemented!"
        event.Skip()

# end of class ExecuteDialog


if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    aboutDialog = StatusDialog(None, -1, "")
    app.SetTopWindow(aboutDialog)
    aboutDialog.Show()
    app.MainLoop()
