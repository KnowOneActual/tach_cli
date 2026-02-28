from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Thresholds:
    yellow: int = 300
    red: int = 120
    soft_overrun: int = 120


@dataclass(frozen=True)
class Position:
    horizontal: str = "center"
    vertical: str = "center"


@dataclass(frozen=True)
class General:
    bold: bool = True


@dataclass(frozen=True)
class Config:
    general: General = field(default_factory=General)
    position: Position = field(default_factory=Position)
    thresholds: Thresholds = field(default_factory=Thresholds)
    profiles: dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class TimerSpec:
    hours: int = 0
    minutes: int = 5
    seconds: int = 0
    kill: bool = False
    profile: str | None = None

    @property
    def total_seconds(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds
