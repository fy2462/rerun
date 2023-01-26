from rerun.log.text import LogLevel

import rerun as rr


def test_text() -> None:
    rr.log_text_entry("path", "text", level=None)
    rr.log_text_entry("path", "text", level=LogLevel.INFO)
    rr.log_text_entry("path", None, level=LogLevel.INFO)  # type: ignore[arg-type]
