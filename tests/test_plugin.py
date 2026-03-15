

def test_plugin_import():
    from report_gen_plugin import ReportGenPlugin

    plugin = ReportGenPlugin()
    assert plugin.name == "report-generator"
