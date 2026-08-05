from datetime import datetime
from typing import List, Optional
import uuid
from sqlModel import Field, Relationship, SQLModel


class Agency(SQLModel, table=True):
  __tablename__ = "agencies"

  id: uuid.UUID = Field(
      default_factory=uuid.uuid4, primary_key=True, nullable=False
  )
  fortnox_agency_id: str = Field(unique=True, index=True, nullable=False)
  name: str = Field(nullable=False)
  created_at: datetime = Field(default_factory=datetime.utcnow)

  # Relation: En byrå kan ha många klienter (tenants)
  tenants: List["Tenant"] = Relationship(back_populates="agency")


class Tenant(SQLModel, table=True):
  __tablename__ = "tenants"

  id: uuid.UUID = Field(
      default_factory=uuid.uuid4, primary_key=True, nullable=False
  )
  agency_id: Optional[uuid.UUID] = Field(
      default=None, foreign_key="agencies.id", ondelete="SET NULL"
  )
  fortnox_tenant_id: str = Field(unique=True, index=True, nullable=False)
  company_name: str = Field(nullable=False)
  created_at: datetime = Field(default_factory=datetime.utcnow)

  # Relations
  agency: Optional[Agency] = Relationship(back_populates="tenants")
  oauth_token: Optional["OAuthToken"] = Relationship(
      back_populates="tenant", sa_relationship_kwargs={"uselist": False}
  )
  recipients: List["ReportRecipient"] = Relationship(
      back_populates="tenant", sa_relationship_kwargs={"cascade": "all, delete"}
  )


class OAuthToken(SQLModel, table=True):
  __tablename__ = "oauth_tokens"

  id: uuid.UUID = Field(
      default_factory=uuid.uuid4, primary_key=True, nullable=False
  )
  tenant_id: uuid.UUID = Field(
      unique=True, foreign_key="tenants.id", ondelete="CASCADE", nullable=False
  )
  enc_refresh_token: str = Field(nullable=False)
  enc_access_token: str = Field(nullable=False)
  access_expires_at: datetime = Field(nullable=False)
  updated_at: datetime = Field(default_factory=datetime.utcnow)

  # Relation
  tenant: Tenant = Relationship(back_populates="oauth_token")


class ReportRecipient(SQLModel, table=True):
  __tablename__ = "report_recipients"

  id: uuid.UUID = Field(
      default_factory=uuid.uuid4, primary_key=True, nullable=False
  )
  tenant_id: uuid.UUID = Field(
      foreign_key="tenants.id", ondelete="CASCADE", nullable=False
  )
  email: str = Field(nullable=False)
  name: Optional[str] = Field(default=None)
  created_at: datetime = Field(default_factory=datetime.utcnow)

  # Relation
  tenant: Tenant = Relationship(back_populates="recipients")