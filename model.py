from sqlalchemy import String, ForeignKey
from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from dataclasses import dataclass


class Base(DeclarativeBase):
    pass


@dataclass
class Blip(Base):
    __tablename__ = "blip"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String)
    slug: Mapped[str] = mapped_column(String, nullable=True)
    parent_id: Mapped[int] = mapped_column(
        ForeignKey("blip.id"), nullable=True
    )  # new line
    blips: Mapped[List["Blip"]] = relationship(
        "Blip",
        back_populates="parent",
        cascade="all, delete-orphan",
        primaryjoin=id == parent_id,  # new line
    )
    parent: Mapped["Blip"] = relationship(
        "Blip",
        back_populates="blips",
        remote_side=[id],  # new line
    )

    def __repr__(self) -> str:
        return f"Blip(id={self.id!r}, content={self.content!r}, author={self.author!r})"
