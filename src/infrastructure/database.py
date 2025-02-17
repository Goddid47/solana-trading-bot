from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SolanaTransaction(Base):
    __tablename__ = 'solana_tx'
    signature = Column(String(88), primary_key=True)
    sender = Column(String(44))
    receiver = Column(String(44))
    amount = Column(JSON)  # Stores lamports and USD value
    timestamp = Column(DateTime)
