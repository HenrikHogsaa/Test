# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, DateTime, Float, Integer, Table, Time, Unicode, text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ActsLoan(Base):
    __tablename__ = 'ActsLoan'

    ActsLoanID = Column(Integer, primary_key=True)
    ReportingDate = Column(Date, nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    PortfolioID = Column(Integer, nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    StartYear = Column(Integer, nullable=False)
    StartMonth = Column(Integer, nullable=False)
    MigInsurance = Column(Boolean, nullable=False)
    PrepaymentAmount = Column(DECIMAL(14, 6))
    MonthsRunning = Column(Integer, nullable=False)
    MonthsRemaining = Column(Integer, nullable=False)
    InArrears = Column(Boolean, nullable=False)
    MonthsInArrearsTime = Column(DECIMAL(14, 6), nullable=False)
    MonthsArrearsWeight = Column(DECIMAL(14, 6), nullable=False)
    MonthsArrearsWeightCap = Column(DECIMAL(14, 6), nullable=False)
    DaysInArrearsTime = Column(DECIMAL(14, 6), nullable=False)
    StartArrears = Column(Date)
    EndArrears = Column(Date)
    ArrearsEventNo = Column(Integer, nullable=False)
    NoPreviousArrears = Column(Integer, nullable=False)
    ProvisionType = Column(Unicode(50), nullable=False)
    Provision = Column(DECIMAL(14, 6), nullable=False)
    ProvisionDelta = Column(DECIMAL(14, 6), nullable=False)
    Cure = Column(Boolean, nullable=False)
    PercentageRecovery = Column(DECIMAL(14, 6), nullable=False)
    InitialPropertyValue = Column(DECIMAL(14, 6), nullable=False)
    IndexedPropertyValue = Column(DECIMAL(14, 6), nullable=False)
    IndexPropertyValueRa1 = Column(DECIMAL(14, 6), nullable=False)
    IndexPropertyValueRa2 = Column(DECIMAL(14, 6), nullable=False)
    InitialLtv = Column(DECIMAL(14, 6), nullable=False)
    IndexedLtv = Column(DECIMAL(14, 6), nullable=False)
    IndexedLtvRa1 = Column(DECIMAL(14, 6), nullable=False)
    IndexedLtvRa2 = Column(DECIMAL(14, 6), nullable=False)
    InitialOC = Column(DECIMAL(14, 6), nullable=False)
    InitialRf = Column(DECIMAL(14, 6), nullable=False)
    InitialMargin = Column(DECIMAL(14, 6), nullable=False)
    RequiredOC = Column(DECIMAL(14, 6), nullable=False)
    RequiredRf = Column(DECIMAL(14, 6), nullable=False)
    FactorA1 = Column(DECIMAL(14, 6), nullable=False)
    FactorA2 = Column(DECIMAL(14, 6), nullable=False)
    OcRatingAgency1 = Column(DECIMAL(14, 6), nullable=False)
    OcRatingAgency2 = Column(DECIMAL(14, 6), nullable=False)
    RWA = Column(DECIMAL(14, 6), nullable=False)
    LtvExcess = Column(DECIMAL(14, 6), nullable=False)
    CreditRiskCapital = Column(DECIMAL(14, 6), nullable=False)
    MarketRiskCapital = Column(DECIMAL(14, 6), nullable=False)
    OperationalRiskCapital = Column(DECIMAL(14, 6), nullable=False)
    OtherCapital = Column(DECIMAL(14, 6), nullable=False)
    TotalCapital = Column(DECIMAL(14, 6), nullable=False)
    Initial_LoanAmount = Column(DECIMAL(14, 6), nullable=False)
    Initial_BondPrincipal = Column(DECIMAL(14, 6), nullable=False)
    Initial_DeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    Initial_DeferredLiability = Column(DECIMAL(14, 6), nullable=False)
    LoanAmount = Column(DECIMAL(14, 6), nullable=False)
    BondPrincipal = Column(DECIMAL(14, 6), nullable=False)
    DeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    DeferredLiability = Column(DECIMAL(14, 6), nullable=False)
    LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    JnCost = Column(DECIMAL(14, 6), nullable=False)
    PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    CreditEL = Column(DECIMAL(14, 6), nullable=False)
    OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    Installment = Column(DECIMAL(14, 6), nullable=False)
    DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    DlContribution = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanAmount = Column(DECIMAL(14, 6), nullable=False)
    MB_BondPrincipal = Column(DECIMAL(14, 6), nullable=False)
    MB_DeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    MB_DeferredLiability = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    MB_CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    MB_Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    MB_JnCost = Column(DECIMAL(14, 6), nullable=False)
    MB_PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    MB_PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    MB_CreditEL = Column(DECIMAL(14, 6), nullable=False)
    MB_OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    MB_Installment = Column(DECIMAL(14, 6), nullable=False)
    MB_DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    MB_DlContribution = Column(DECIMAL(14, 6), nullable=False)
    Coll_LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    Coll_CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Coll_Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    Coll_JnCost = Column(DECIMAL(14, 6), nullable=False)
    Coll_PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    Coll_PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    Coll_CreditEL = Column(DECIMAL(14, 6), nullable=False)
    Coll_OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    Coll_LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    Coll_Installment = Column(DECIMAL(14, 6), nullable=False)
    Coll_DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Coll_DlContribution = Column(DECIMAL(14, 6), nullable=False)
    Coll_BondRedemption = Column(DECIMAL(14, 6), nullable=False)
    Coll_PartnerBankFees = Column(DECIMAL(14, 6), nullable=False)
    Coll_DppRedemption = Column(DECIMAL(14, 6), nullable=False)
    BondInterest = Column(DECIMAL(14, 6), nullable=False)
    BondCapital = Column(DECIMAL(14, 6), nullable=False)
    BondPayment = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class ActsLoanPart(Base):
    __tablename__ = 'ActsLoanPart'

    ActsLoanPartID = Column(Integer, primary_key=True)
    ReportingDate = Column(Date, nullable=False)
    PortfolioID = Column(Integer, nullable=False)
    LoanTypeNumber = Column(Integer, nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    LoanPartNumber = Column(Integer, nullable=False)
    LoanProductID = Column(Integer, nullable=False)
    IsinNumber = Column(Integer, nullable=False)
    Coupon = Column(DECIMAL(14, 6), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    StartYear = Column(Integer, nullable=False)
    StartMonth = Column(Integer, nullable=False)
    Tenor = Column(Integer, nullable=False)
    IoPeriod = Column(Integer, nullable=False)
    PrepaymentDate = Column(Date)
    PrepaymentAmount = Column(DECIMAL(14, 6))
    PrepaymentType = Column(Unicode(50), nullable=False)
    MonthsRunning = Column(Integer, nullable=False)
    MonthsRemaining = Column(Integer, nullable=False)
    MonthsInArrearsTime = Column(DECIMAL(14, 6), nullable=False)
    MonthsArrearsWeight = Column(DECIMAL(14, 6), nullable=False)
    MonthsArrearsWeightCap = Column(DECIMAL(14, 6), nullable=False)
    DaysInArrearsTime = Column(DECIMAL(14, 6), nullable=False)
    Cure = Column(Boolean, nullable=False)
    StartArrears = Column(Date)
    EndArrears = Column(Date)
    Initial_LoanAmount = Column(DECIMAL(14, 6), nullable=False)
    Initial_BondPrincipal = Column(DECIMAL(14, 6), nullable=False)
    Initial_DeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    Initial_DeferredLiability = Column(DECIMAL(14, 6), nullable=False)
    LoanAmount = Column(DECIMAL(14, 6), nullable=False)
    BondPrincipal = Column(DECIMAL(14, 6), nullable=False)
    DeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    DeferredLiability = Column(DECIMAL(14, 6), nullable=False)
    LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    JnCost = Column(DECIMAL(14, 6), nullable=False)
    PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    CreditEL = Column(DECIMAL(14, 6), nullable=False)
    OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    Installment = Column(DECIMAL(14, 6), nullable=False)
    DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    DlContribution = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanAmount = Column(DECIMAL(14, 6), nullable=False)
    MB_BondPrincipal = Column(DECIMAL(14, 6), nullable=False)
    MB_DeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    MB_DeferredLiability = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    MB_CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    MB_Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    MB_JnCost = Column(DECIMAL(14, 6), nullable=False)
    MB_PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    MB_PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    MB_CreditEL = Column(DECIMAL(14, 6), nullable=False)
    MB_OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    MB_Installment = Column(DECIMAL(14, 6), nullable=False)
    MB_DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    MB_DlContribution = Column(DECIMAL(14, 6), nullable=False)
    Coll_LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    Coll_CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Coll_Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    Coll_JnCost = Column(DECIMAL(14, 6), nullable=False)
    Coll_PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    Coll_PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    Coll_CreditEL = Column(DECIMAL(14, 6), nullable=False)
    Coll_OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    Coll_LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    Coll_Installment = Column(DECIMAL(14, 6), nullable=False)
    Coll_DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Coll_DlContribution = Column(DECIMAL(14, 6), nullable=False)
    Coll_BondRedemption = Column(DECIMAL(14, 6), nullable=False)
    Coll_PartnerBankFees = Column(DECIMAL(14, 6), nullable=False)
    Coll_DppRedemption = Column(DECIMAL(14, 6), nullable=False)
    BondInterest = Column(DECIMAL(14, 6), nullable=False)
    BondCapital = Column(DECIMAL(14, 6), nullable=False)
    BondPayment = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class AmortisationScheme(Base):
    __tablename__ = 'AmortisationScheme'

    AmortisationSchemeID = Column(Integer, primary_key=True)
    LoanNumber = Column(Integer, nullable=False)
    LoanPartNumber = Column(Integer, nullable=False)
    LoanDueDate = Column(Date, nullable=False)
    LoanBalanceBop = Column(DECIMAL(14, 2), nullable=False)
    LoanInterest = Column(DECIMAL(14, 2), nullable=False)
    CustDaAmortisation = Column(DECIMAL(14, 2), nullable=False)
    Cet1Cost = Column(DECIMAL(14, 2), nullable=False)
    JnCost = Column(DECIMAL(14, 2), nullable=False)
    PerennaFee = Column(DECIMAL(14, 2), nullable=False)
    PbServicingFee = Column(DECIMAL(14, 2), nullable=False)
    PbOriginationFee = Column(DECIMAL(14, 2), nullable=False)
    PipelineEL = Column(DECIMAL(14, 2), nullable=False)
    PrepaymentCost = Column(DECIMAL(14, 2), nullable=False)
    CreditEL = Column(DECIMAL(14, 2), nullable=False)
    OperationRiskEl = Column(DECIMAL(14, 2), nullable=False)
    LoanCapital = Column(DECIMAL(14, 2), nullable=False)
    Installment = Column(DECIMAL(14, 2), nullable=False)
    LoanBalanceEop = Column(DECIMAL(14, 2), nullable=False)
    BondDueDate = Column(Date, nullable=False)
    BondBalanceBop = Column(DECIMAL(14, 2), nullable=False)
    BondInterest = Column(DECIMAL(14, 2), nullable=False)
    BondCapital = Column(DECIMAL(14, 2), nullable=False)
    BondPayment = Column(DECIMAL(14, 2), nullable=False)
    BondBalanceEop = Column(DECIMAL(14, 2), nullable=False)
    DaBop = Column(DECIMAL(14, 2), nullable=False)
    DaAmortisation = Column(DECIMAL(14, 2), nullable=False)
    DaEop = Column(DECIMAL(14, 2), nullable=False)
    DlBop = Column(DECIMAL(14, 2), nullable=False)
    DlContribution = Column(DECIMAL(14, 2), nullable=False)
    DlEop = Column(DECIMAL(14, 2), nullable=False)
    Version = Column(Integer, nullable=False)
    ValidFrom = Column(DateTime, nullable=False)
    ValidUntil = Column(DateTime, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class ArrearsLoan(Base):
    __tablename__ = 'ArrearsLoan'

    ArrearsLoanID = Column(Integer, primary_key=True)
    ReportingDate = Column(Date, nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    Status = Column(Unicode(50), nullable=False)
    MonthsInArrearsTime = Column(DECIMAL(14, 6), nullable=False)
    MonthsArrearsWeight = Column(DECIMAL(14, 6), nullable=False)
    MonthsArrearsWeightCap = Column(DECIMAL(14, 6), nullable=False)
    DaysInArrearsTime = Column(DECIMAL(14, 6), nullable=False)
    StartArrears = Column(Date, nullable=False)
    EndArrears = Column(Date, nullable=False)
    ArrearsEventNo = Column(Integer, nullable=False)
    NoPreviousArrears = Column(Integer, nullable=False)
    ProvisionType = Column(Unicode(50), nullable=False)
    Provision = Column(DECIMAL(14, 6), nullable=False)
    ProvisionDelta = Column(DECIMAL(14, 6), nullable=False)
    Cure = Column(Boolean, nullable=False)
    MB_LoanAmount = Column(DECIMAL(14, 6), nullable=False)
    MB_BondPrincipal = Column(DECIMAL(14, 6), nullable=False)
    MB_DeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    MB_DeferredLiability = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    MB_CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    MB_Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    MB_JnCost = Column(DECIMAL(14, 6), nullable=False)
    MB_PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    MB_PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    MB_CreditEL = Column(DECIMAL(14, 6), nullable=False)
    MB_OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    MB_Installment = Column(DECIMAL(14, 6), nullable=False)
    MB_DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    MB_DlContribution = Column(DECIMAL(14, 6), nullable=False)
    Coll_LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    Coll_CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Coll_Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    Coll_JnCost = Column(DECIMAL(14, 6), nullable=False)
    Coll_PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    Coll_PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    Coll_CreditEL = Column(DECIMAL(14, 6), nullable=False)
    Coll_OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    Coll_LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    Coll_Installment = Column(DECIMAL(14, 6), nullable=False)
    Coll_DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Coll_DlContribution = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class ArrearsLoanPart(Base):
    __tablename__ = 'ArrearsLoanPart'

    ArrearsLoanPartID = Column(Integer, primary_key=True)
    ReportingDate = Column(Date, nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    LoanPartNumber = Column(Integer, nullable=False)
    Status = Column(Unicode(50), nullable=False)
    MonthsInArrearsTime = Column(DECIMAL(14, 6), nullable=False)
    MonthsArrearsWeight = Column(DECIMAL(14, 6), nullable=False)
    MonthsArrearsWeightCap = Column(DECIMAL(14, 6), nullable=False)
    DaysInArrearsTime = Column(DECIMAL(14, 6), nullable=False)
    StartArrears = Column(Date, nullable=False)
    EndArrears = Column(Date, nullable=False)
    ArrearsEventNo = Column(Integer, nullable=False)
    NoPreviousArrears = Column(Integer, nullable=False)
    Cure = Column(Boolean, nullable=False)
    MB_LoanAmount = Column(DECIMAL(14, 6), nullable=False)
    MB_BondPrincipal = Column(DECIMAL(14, 6), nullable=False)
    MB_DeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    MB_DeferredLiability = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    MB_CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    MB_Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    MB_JnCost = Column(DECIMAL(14, 6), nullable=False)
    MB_PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    MB_PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    MB_PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    MB_CreditEL = Column(DECIMAL(14, 6), nullable=False)
    MB_OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    MB_LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    MB_Installment = Column(DECIMAL(14, 6), nullable=False)
    MB_DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    MB_DlContribution = Column(DECIMAL(14, 6), nullable=False)
    Coll_LoanInterest = Column(DECIMAL(14, 6), nullable=False)
    Coll_CustDaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Coll_Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    Coll_JnCost = Column(DECIMAL(14, 6), nullable=False)
    Coll_PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    Coll_PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    Coll_PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    Coll_CreditEL = Column(DECIMAL(14, 6), nullable=False)
    Coll_OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    Coll_LoanCapital = Column(DECIMAL(14, 6), nullable=False)
    Coll_Installment = Column(DECIMAL(14, 6), nullable=False)
    Coll_DaAmortisation = Column(DECIMAL(14, 6), nullable=False)
    Coll_DlContribution = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class BondLedger(Base):
    __tablename__ = 'BondLedger'

    BondLedgerID = Column(Integer, primary_key=True)
    IsinNumber = Column(Integer, nullable=False)
    TransactionType = Column(Unicode(50), nullable=False)
    NominalAmount = Column(DECIMAL(14, 2), nullable=False)
    TransactionDate = Column(DateTime, nullable=False)
    BondTradeNumber = Column(Integer)
    SettlementDate = Column(Date, nullable=False)
    Status = Column(Unicode(50), nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class BondPrice(Base):
    __tablename__ = 'BondPrice'

    BondPriceID = Column(Integer, primary_key=True)
    Date = Column(DateTime, nullable=False)
    IsinNumber = Column(Integer, nullable=False)
    MarketMakerID = Column(Integer, nullable=False)
    Bid = Column(DECIMAL(14, 6), nullable=False)
    Ask = Column(DECIMAL(14, 6), nullable=False)
    Mid = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class BondTrade(Base):
    __tablename__ = 'BondTrade'

    BondTradeID = Column(Integer, primary_key=True)
    BondTradeNumber = Column(Integer, nullable=False)
    IsinNumber = Column(Integer, nullable=False)
    MarketMakerID = Column(Integer, nullable=False)
    Status = Column(Unicode(50), nullable=False)
    BondNextCouponPaymentDate = Column(Date, nullable=False)
    BondPreviousCouponPaymentDate = Column(Date, nullable=False)
    TradeDate = Column(DateTime, nullable=False)
    TradeType = Column(Unicode(50), nullable=False)
    TradePrice = Column(DECIMAL(14, 6), nullable=False)
    NominalTradingBondAmount = Column(DECIMAL(14, 6), nullable=False)
    CleanValue = Column(DECIMAL(14, 6), nullable=False)
    AccruedInterest = Column(DECIMAL(14, 6), nullable=False)
    Commission = Column(DECIMAL(14, 6), nullable=False)
    SettlementDate = Column(DECIMAL(14, 6), nullable=False)
    SettlementAmount = Column(DECIMAL(14, 6), nullable=False)
    AllocationStatus = Column(Unicode(50), nullable=False)
    BondTradeAllocation = Column(DateTime, nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class BondYield(Base):
    __tablename__ = 'BondYield'

    BondYieldID = Column(Integer, primary_key=True)
    BondYieldDate = Column(DateTime, nullable=False)
    BondYield = Column(DECIMAL(14, 6), nullable=False)
    TenorID = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class CustomerPrice(Base):
    __tablename__ = 'CustomerPrice'

    CustomerPriceID = Column(Integer, primary_key=True)
    CustomerPriceDate = Column(DateTime, nullable=False)
    IsinNumber = Column(Integer, nullable=False)
    CustomerBid = Column(DECIMAL(14, 6), nullable=False)
    CustomerAsk = Column(DECIMAL(14, 6), nullable=False)
    NumberInAverage = Column(Integer, nullable=False)
    ApprovedStatus = Column(Unicode(50), nullable=False)
    LogID = Column(Unicode(50), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class FullPrepayment(Base):
    __tablename__ = 'FullPrepayment'

    FullPrepaymentID = Column(Integer, primary_key=True)
    PrepaymentDate = Column(Date, nullable=False)
    LoanPartNumber = Column(Integer, nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    ReductionInLoanBalance = Column(DECIMAL(14, 6), nullable=False)
    ReductionInBondBalance = Column(DECIMAL(14, 6), nullable=False)
    FixedPrepaymentFee = Column(DECIMAL(14, 6), nullable=False)
    ErcAmount = Column(DECIMAL(14, 6), nullable=False)
    VariablePrepaymentFee = Column(DECIMAL(14, 6), nullable=False)
    BondInterestUnderPmtPrepaymentMonth = Column(DECIMAL(14, 6), nullable=False)
    BondInterestUnderPmtNextMonth = Column(DECIMAL(14, 6), nullable=False)
    DaAmortisationUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    Cet1CostUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    JnCostUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    PerennaFeeUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    PbServicingFeeUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    PbOriginationFeeUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    PipelineELUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    PrepaymentCostUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    CreditELUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    OperationRiskElUnderPmt = Column(DECIMAL(14, 6), nullable=False)
    RiskFreeInterestReceived = Column(DECIMAL(14, 6), nullable=False)
    TotalMarginAdjustment = Column(DECIMAL(14, 6), nullable=False)
    UseCallOption = Column(DECIMAL(14, 6), nullable=False)
    RedemptionAmountPrepaymentMonth = Column(DECIMAL(14, 6), nullable=False)
    PerennaBondInterestPmtPrepaymentMonth = Column(DECIMAL(14, 6), nullable=False)
    RedemptionAmountNextMonth = Column(DECIMAL(14, 6), nullable=False)
    PerennaBondInterestPmtNextMonth = Column(DECIMAL(14, 6), nullable=False)
    AmountReceivedFromBorrower = Column(DECIMAL(14, 6), nullable=False)
    DeferredAssetPaidByBorrower = Column(DECIMAL(14, 6), nullable=False)
    TotalPrepaymentAmount = Column(DECIMAL(14, 6), nullable=False)
    BondInterestFromSettlementDate = Column(DECIMAL(14, 6), nullable=False)
    BondPurchaseAmount = Column(DECIMAL(14, 6), nullable=False)
    PerennaFinancialResult = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class GeneralLedger(Base):
    __tablename__ = 'GeneralLedger'

    GeneralLedgerID = Column(Integer, primary_key=True)
    ReportingDate = Column(Date, nullable=False)
    PortolioID = Column(Integer, nullable=False)
    IcPortfolioID = Column(Integer)
    Ledger = Column(Unicode(3), nullable=False)
    IcLedger = Column(Unicode(3))
    LoanNumber = Column(Integer, nullable=False)
    LoanPartNumber = Column(Integer, nullable=False)
    Account = Column(Integer, nullable=False)
    Balance = Column(DECIMAL(16, 2), nullable=False)
    IsinNumber = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class InitialInterestAllocation(Base):
    __tablename__ = 'InitialInterestAllocation'

    InitialInterestAllocationID = Column(Integer, primary_key=True)
    LoanPartNumber = Column(Integer, nullable=False)
    RowNo = Column(Integer, nullable=False)
    Date = Column(Date, nullable=False)
    AccruedInterestMarketMaker = Column(DECIMAL(14, 6), nullable=False)
    TreasuryInterestLoss = Column(DECIMAL(14, 6), nullable=False)
    AccruedInterestForwardAgreementTreasury = Column(DECIMAL(14, 6), nullable=False)
    AccruedInterestForwardAgreementOperations = Column(DECIMAL(14, 6), nullable=False)
    TreasuryIssuesBond = Column(DECIMAL(14, 6), nullable=False)
    TreasurySellsBond = Column(DECIMAL(14, 6), nullable=False)
    TreasuryCashAccountToOperations = Column(DECIMAL(14, 6), nullable=False)
    TreasuryCashAccountToInvestors = Column(DECIMAL(14, 6), nullable=False)
    TotalAccruedInterest = Column(DECIMAL(14, 6), nullable=False)
    RiskFreeInterestTreasury = Column(DECIMAL(14, 6), nullable=False)
    RiskFreeInterestOperations = Column(DECIMAL(14, 6), nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class Isin(Base):
    __tablename__ = 'Isin'

    IsinID = Column(Integer, primary_key=True)
    BondTypeID = Column(Integer, nullable=False)
    IsinNumber = Column(Integer, nullable=False)
    Description = Column(Unicode(150), nullable=False)
    TapOpeningDate = Column(Date, nullable=False)
    TapClosingDate = Column(Date, nullable=False)
    OpeningDate = Column(Date, nullable=False)
    ClosingDate = Column(Date, nullable=False)
    Coupon = Column(DECIMAL(14, 6), nullable=False)
    TenorID = Column(Integer, nullable=False)
    MinLoanTenor = Column(Integer, nullable=False)
    LegalMaturityDate = Column(Date, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class JournalEntry(Base):
    __tablename__ = 'JournalEntries'

    JournalEntryId = Column(Integer, primary_key=True)
    ValueDate = Column(Date, nullable=False)
    PortolioID = Column(Integer, nullable=False)
    IcPortfolioID = Column(Integer)
    Ledger = Column(Unicode(3), nullable=False)
    IcLedger = Column(Unicode(3))
    LoanNumber = Column(Integer, nullable=False)
    LoanPartNumber = Column(Integer, nullable=False)
    Account = Column(Integer, nullable=False)
    Amount = Column(DECIMAL(16, 2), nullable=False)
    DC = Column(Unicode(1), nullable=False)
    EventNo = Column(Integer, nullable=False)
    IsinNumber = Column(Integer, nullable=False)
    BookingEntryNo = Column(Integer, nullable=False)
    Timestamp = Column(DateTime, nullable=False)


class Loan(Base):
    __tablename__ = 'Loan'

    LoanID = Column(Integer, primary_key=True)
    PortfolioID = Column(Integer, nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    Mig = Column(Boolean, nullable=False)
    LoanAmount = Column(DECIMAL(14, 2), nullable=False)
    PropertyValue = Column(DECIMAL(14, 2), nullable=False)
    InitialLtv = Column(DECIMAL(14, 2), nullable=False)
    ClosingCost = Column(DECIMAL(14, 2), nullable=False)
    PartnerBankClosingCost = Column(DECIMAL(14, 2), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    CompletionDate = Column(Date, nullable=False)
    Status = Column(Unicode(50), nullable=False)
    DipDate = Column(Date, nullable=False)
    OfferDate = Column(Date, nullable=False)
    FixingDate = Column(DateTime, nullable=False)
    InitialOC = Column(DECIMAL(14, 2), nullable=False)
    InitialRF = Column(DECIMAL(14, 2), nullable=False)
    CustomerMargin = Column(DECIMAL(14, 2), nullable=False)
    LoanYield = Column(DECIMAL(14, 2), nullable=False)
    ValidFrom = Column(DateTime, nullable=False)
    ValidUntil = Column(DateTime, nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class LoanBondAllocation(Base):
    __tablename__ = 'LoanBondAllocation'

    LoanBondAllocationID = Column(Integer, primary_key=True)
    BondTradeNumber = Column(Integer)
    LoanPartNumber = Column(Integer)
    NettingId = Column(Integer)
    AllocationAmount = Column(DECIMAL(14, 2), nullable=False)
    AllocationDate = Column(DateTime, nullable=False)
    AllocationPrice = Column(DECIMAL(14, 2), nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class LoanPartBondline(Base):
    __tablename__ = 'LoanPartBondline'

    LoanPartBondlineID = Column(Integer, primary_key=True)
    LoanTypeNumber = Column(Integer, nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    LoanPartNumber = Column(Integer, nullable=False)
    LoanAmount = Column(DECIMAL(14, 2), nullable=False)
    Tenor = Column(Integer, nullable=False)
    IoPeriod = Column(Integer, nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    DipDate = Column(Date, nullable=False)
    OfferDate = Column(Date, nullable=False)
    FixingDate = Column(DateTime, nullable=False)
    FixingPriceDate = Column(DateTime, nullable=False)
    FixingSettlementDate = Column(Date, nullable=False)
    Status = Column(Unicode(50), nullable=False)
    AllocationStatus = Column(Unicode(50))
    IsinNumber = Column(Integer, nullable=False)
    BondPrincipal = Column(DECIMAL(14, 2), nullable=False)
    BondAction = Column(Unicode(50), nullable=False)
    ForwardBondInterest = Column(DECIMAL(14, 2), nullable=False)
    ForwardRiskFreeInterest = Column(DECIMAL(14, 2), nullable=False)
    RemainingOnAccount = Column(DECIMAL(14, 2), nullable=False)
    NeedExtraCash = Column(DECIMAL(14, 2), nullable=False)
    FixingPrice = Column(DECIMAL(14, 2), nullable=False)
    FixingSpotPrice = Column(DECIMAL(14, 2), nullable=False)
    YieldPerMonth = Column(DECIMAL(14, 2), nullable=False)
    YieldPerMonthDA = Column(DECIMAL(14, 2), nullable=False)
    AnnualYield = Column(DECIMAL(14, 2), nullable=False)
    AnnualYieldDA = Column(DECIMAL(14, 2), nullable=False)
    MonthlyPayment = Column(DECIMAL(14, 2), nullable=False)
    MonthlyPaymentDA = Column(DECIMAL(14, 2), nullable=False)
    CapitalPmtFirstMonth = Column(Boolean, nullable=False)
    AllocationDate = Column(DateTime, nullable=False)
    AllocationSettlementDate = Column(DateTime, nullable=False)
    BondTradeAccrued = Column(DECIMAL(14, 2), nullable=False)
    BondBondTradeNetAccrued = Column(DECIMAL(14, 2), nullable=False)
    BondTradeInterest = Column(DECIMAL(14, 2), nullable=False)
    BondTradeSpotPrice = Column(DECIMAL(14, 2), nullable=False)
    BondTradeMarketValue = Column(DECIMAL(14, 2), nullable=False)
    AllocationAccrued = Column(DECIMAL(14, 2), nullable=False)
    AllocationNetAccrued = Column(DECIMAL(14, 2), nullable=False)
    AllocationInterest = Column(DECIMAL(14, 2), nullable=False)
    AllocationCapitalGain = Column(DECIMAL(14, 2), nullable=False)
    AllocationCarry = Column(DECIMAL(14, 2), nullable=False)
    ValidFrom = Column(DateTime, nullable=False)
    ValidUntil = Column(DateTime, nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class LoanType(Base):
    __tablename__ = 'LoanType'

    LoanTypeID = Column(Integer, primary_key=True)
    LoanType = Column(Unicode(50), nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    LoanProductID = Column(Integer, nullable=False)
    LoanTypeNumber = Column(Integer, nullable=False)
    LoanTypeAmount = Column(DECIMAL(14, 2), nullable=False)
    ValidFrom = Column(DateTime, nullable=False)
    ValidUntil = Column(DateTime, nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PFSArrearsSetting(Base):
    __tablename__ = 'PFS_ArrearsSettings'

    ArrearsSettingID = Column(Integer, primary_key=True)
    EconomicScenarioID = Column(Integer, nullable=False)
    ReportingDate = Column(Date, nullable=False)
    ArrearsPercentage = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PFSBankSetting(Base):
    __tablename__ = 'PFS_BankSettings'

    BankSettingID = Column(Integer, primary_key=True)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    LastStartDayInMonth = Column(Integer, nullable=False)
    TargetAdditionalOC = Column(DECIMAL(14, 6), nullable=False)
    PercHavingOneLoanPart = Column(DECIMAL(14, 6), nullable=False)
    PerformGainDrivenPrepayments = Column(Boolean, nullable=False)
    CPR = Column(DECIMAL(14, 6), nullable=False)
    minMonthsServicing = Column(Integer, nullable=False)
    maxNoPartialPrepayments = Column(Integer, nullable=False)
    MinPartialPrepaymentPercentage = Column(DECIMAL(14, 6), nullable=False)
    MaxPartialPrepaymentPercentage = Column(DECIMAL(14, 6), nullable=False)
    CurePeriod = Column(Integer, nullable=False)
    ForeclosurePeriod = Column(Integer, nullable=False)
    ForeclosureCosts = Column(DECIMAL(14, 6), nullable=False)
    provPD0 = Column(DECIMAL(14, 6), nullable=False)
    provPD1 = Column(DECIMAL(14, 6), nullable=False)
    provPD2 = Column(DECIMAL(14, 6), nullable=False)
    provPD3 = Column(DECIMAL(14, 6), nullable=False)
    provMVD = Column(DECIMAL(14, 6), nullable=False)
    MarketValueDecline = Column(DECIMAL(14, 6), nullable=False)
    LtvLimit = Column(DECIMAL(14, 6), nullable=False)
    JuniorNoteSpread = Column(DECIMAL(14, 6), nullable=False)
    JuniorNoteSpreadCorrelation = Column(DECIMAL(14, 6), nullable=False)
    ActPercentageRa1 = Column(DECIMAL(14, 6), nullable=False)
    ActPercentageRa2 = Column(DECIMAL(14, 6), nullable=False)
    RatingAgency1Ubound = Column(DECIMAL(14, 6), nullable=False)
    RatingAgency1Lbound = Column(DECIMAL(14, 6), nullable=False)
    RatingAgency2Ubound = Column(DECIMAL(14, 6), nullable=False)
    RatingAgency2Lbound = Column(DECIMAL(14, 6), nullable=False)
    RatingAgency1HpiUp = Column(DECIMAL(14, 6), nullable=False)
    RatingAgency2HpiUp = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PFSCet1Percentage(Base):
    __tablename__ = 'PFS_Cet1Percentage'

    Cet1PercentageID = Column(Integer, primary_key=True)
    Year = Column(Integer, nullable=False)
    Percentage = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PFSEconomicScenario(Base):
    __tablename__ = 'PFS_EconomicScenarios'

    EconomicScenarioID = Column(Integer, primary_key=True)
    ScenarioDescription = Column(Unicode(50), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PFSGainPrepaymentSetting(Base):
    __tablename__ = 'PFS_GainPrepaymentSettings'

    GainPrepaymentSettingsID = Column(Integer, primary_key=True)
    LowerBoundary = Column(DECIMAL(14, 6), nullable=False)
    UpperBoundary = Column(DECIMAL(14, 6), nullable=False)
    Percentage = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PFSLtvSetting(Base):
    __tablename__ = 'PFS_LtvSettings'

    LtvSettingID = Column(Integer, primary_key=True)
    LtvBucket = Column(Integer, nullable=False)
    NumberOfLoans = Column(Integer, nullable=False)
    PortfolioID = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PFSOcRequirement(Base):
    __tablename__ = 'PFS_OcRequirements'

    OcRequirementId = Column(Integer, primary_key=True)
    PD = Column(Float(53), nullable=False)
    LTV = Column(Float(53), nullable=False)
    ReserveFund = Column(Float(53), nullable=False)
    EcAaa = Column(Float(53), nullable=False)
    EcAa = Column(Float(53), nullable=False)
    EcA = Column(Float(53), nullable=False)
    LgdAaa = Column(Float(53), nullable=False)
    LgdAa = Column(Float(53), nullable=False)
    LgdA = Column(Float(53), nullable=False)
    RWA = Column(Float(53), nullable=False)
    OcFloor = Column(Float(53), nullable=False)
    EcAaaMIG = Column(Float(53), nullable=False, server_default=text("((0))"))
    EcAaMIG = Column(Float(53), nullable=False, server_default=text("((0))"))
    EcAMIG = Column(Float(53), nullable=False, server_default=text("((0))"))
    LgdAaaMIG = Column(Float(53), nullable=False, server_default=text("((0))"))
    LgdAaMIG = Column(Float(53), nullable=False, server_default=text("((0))"))
    LgdAMIG = Column(Float(53), nullable=False, server_default=text("((0))"))
    OcFloorMIG = Column(Float(53), nullable=False, server_default=text("((0))"))
    TimeStamp = Column(DateTime, nullable=False)


class PFSPipelinePortfolioSetting(Base):
    __tablename__ = 'PFS_PipelinePortfolioSettings'

    PipelinePortfolioSettingID = Column(Integer, primary_key=True)
    LoanStartDate = Column(Date, nullable=False)
    LoanEndDate = Column(Date, nullable=False)
    LoanAvgAppsPerDay = Column(Integer, nullable=False)
    NoPortfolios = Column(Integer, nullable=False)
    MaxDaysOffer = Column(Integer, nullable=False)
    MaxDaysOfferFixing = Column(Integer, nullable=False)
    NoDaysFixingToCompletion = Column(Integer, nullable=False)
    NoDaysFundingToCompletion = Column(Integer, nullable=False)
    PercentageCancelled = Column(DECIMAL(14, 6), nullable=False)
    PercentageCancelledImmediately = Column(DECIMAL(14, 6), nullable=False)
    MaxFixingToCancel = Column(Integer, nullable=False)
    LoanMinAmount = Column(DECIMAL(14, 6), nullable=False)
    LoanMaxAmount = Column(DECIMAL(14, 6), nullable=False)
    LTV = Column(DECIMAL(14, 6), nullable=False)
    ForwardCommission = Column(Integer, nullable=False)
    PerennaOriginationFee = Column(Integer, nullable=False)
    PercentageMig = Column(DECIMAL(14, 6), nullable=False)
    MinimumBondTradeAmount = Column(DECIMAL(14, 6), nullable=False)
    ApplyRoundedTradeVolumes = Column(Boolean, nullable=False)
    BondTradeBlockSize = Column(DECIMAL(14, 6), nullable=False)
    SettlementDays = Column(Integer, nullable=False)
    MaxOpenPosition = Column(DECIMAL(14, 6), nullable=False)
    PrefundingAllowed = Column(Boolean, nullable=False)
    MinPrefundingAmount = Column(DECIMAL(14, 6), nullable=False)
    MaxPrefundingAmount = Column(DECIMAL(14, 6), nullable=False)
    ApplyBondTradeNetting = Column(Boolean, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PFSPortfolioSetting(Base):
    __tablename__ = 'PFS_PortfolioSettings'

    PortfolioSettingID = Column(Integer, primary_key=True)
    Year = Column(Integer, nullable=False)
    cureRateMonth1 = Column(DECIMAL(14, 6), nullable=False)
    cureRateMonth2 = Column(DECIMAL(14, 6), nullable=False)
    cureRateMonth3 = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class PartialPrepayment(Base):
    __tablename__ = 'PartialPrepayment'

    PartialPrepaymentID = Column(Integer, primary_key=True)
    PrepaymentDate = Column(Date, nullable=False)
    LoanPartNumber = Column(Integer, nullable=False)
    LoanNumber = Column(Integer, nullable=False)
    GrossPrepaymentAmount = Column(DECIMAL(14, 6), nullable=False)
    FixedPrepaymentFee = Column(DECIMAL(14, 6), nullable=False)
    ErcAmount = Column(DECIMAL(14, 6), nullable=False)
    VariablePrepaymentFee = Column(DECIMAL(14, 6), nullable=False)
    PrepaymentAfterFees = Column(DECIMAL(14, 6), nullable=False)
    ReductionInLoanBalance = Column(DECIMAL(14, 6), nullable=False)
    NewLoanBalance = Column(DECIMAL(14, 6), nullable=False)
    ReductionInBondBalance = Column(DECIMAL(14, 6), nullable=False)
    NewBondBalance = Column(DECIMAL(14, 6), nullable=False)
    ReductionInDeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    NewDeferredAsset = Column(DECIMAL(14, 6), nullable=False)
    LoanInterestOverPmt = Column(DECIMAL(14, 6), nullable=False)
    DaAmortisationOverPmt = Column(DECIMAL(14, 6), nullable=False)
    Cet1CostOverPmt = Column(DECIMAL(14, 6), nullable=False)
    JnCostOverPmt = Column(DECIMAL(14, 6), nullable=False)
    PerennaFeeOverPmt = Column(DECIMAL(14, 6), nullable=False)
    PbServicingFeeOverPmt = Column(DECIMAL(14, 6), nullable=False)
    PbOriginationFeeOverPmt = Column(DECIMAL(14, 6), nullable=False)
    PipelineELOverPmt = Column(DECIMAL(14, 6), nullable=False)
    PrepaymentCostOverPmt = Column(DECIMAL(14, 6), nullable=False)
    CreditELOverPmt = Column(DECIMAL(14, 6), nullable=False)
    OperationRiskElOverPmt = Column(DECIMAL(14, 6), nullable=False)
    RiskFreeInterestReceived = Column(DECIMAL(14, 6), nullable=False)
    RedemptionAmountPrepaymentMonth = Column(DECIMAL(14, 6), nullable=False)
    BondInterestUntilEndOfMonth = Column(DECIMAL(14, 6), nullable=False)
    RedemptionAmountNextMonth = Column(DECIMAL(14, 6), nullable=False)
    BondInterestUntilEndOfNextMonth = Column(DECIMAL(14, 6), nullable=False)
    Fees = Column(DECIMAL(14, 6), nullable=False)
    DeferredAmortisationOverpayment = Column(DECIMAL(14, 6), nullable=False)
    BondInterestPaidByPerenna = Column(DECIMAL(14, 6), nullable=False)
    BondPurchasePrice = Column(DECIMAL(14, 6), nullable=False)
    PerennaFinancialResult = Column(DECIMAL(14, 6), nullable=False)
    LoanYieldExclMargins = Column(DECIMAL(14, 6), nullable=False)
    LoanYieldExclMarginsIo = Column(DECIMAL(14, 6), nullable=False)
    NewMonthlyLoanPmtAmortisingPart = Column(DECIMAL(14, 6), nullable=False)
    NewMonthlyLoanPmtIo = Column(DECIMAL(14, 6), nullable=False)
    AccruedInterestPayable = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class RSBondPriceRunSetting(Base):
    __tablename__ = 'RS_BondPriceRunSetting'

    BondPriceRunSettingID = Column(Integer, primary_key=True)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    BeginOfDay = Column(Time, nullable=False)
    EndOfDay = Column(Time, nullable=False)
    NoPricesPerDay = Column(Integer, nullable=False)
    Volatility = Column(DECIMAL(14, 6), nullable=False)
    ReversionToMean = Column(DECIMAL(14, 6), nullable=False)
    ApplyReversionToMean = Column(Boolean, nullable=False)
    Floor = Column(DECIMAL(14, 6), nullable=False)
    Cap = Column(DECIMAL(14, 6), nullable=False)
    QuotePercentage = Column(DECIMAL(14, 6), nullable=False)
    MaxNoMinutes = Column(Integer, nullable=False)
    MaxDeviation = Column(Integer, nullable=False)
    MinPriceChange = Column(DECIMAL(14, 6), nullable=False)
    MaxPriceChange = Column(DECIMAL(14, 6), nullable=False)
    CouponInterval = Column(DECIMAL(14, 6), nullable=False)
    BidAskSpread = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class RSBondTypeDistribution(Base):
    __tablename__ = 'RS_BondTypeDistribution'

    BondTypeDistributionID = Column(Integer, primary_key=True)
    Percentage = Column(DECIMAL(14, 2), nullable=False)
    BondTypeID = Column(Integer, nullable=False)
    TenorID = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class RSMarginSetting(Base):
    __tablename__ = 'RS_MarginSettings'

    MarginSettingID = Column(Integer, primary_key=True)
    LTV = Column(DECIMAL(14, 6), nullable=False)
    Margin = Column(DECIMAL(14, 6), nullable=False)
    Cet1Cost = Column(DECIMAL(14, 6), nullable=False)
    JnCost = Column(DECIMAL(14, 6), nullable=False)
    PerennaFee = Column(DECIMAL(14, 6), nullable=False)
    PbServicingFee = Column(DECIMAL(14, 6), nullable=False)
    PbOriginationFee = Column(DECIMAL(14, 6), nullable=False)
    PipelineEL = Column(DECIMAL(14, 6), nullable=False)
    PrepaymentCost = Column(DECIMAL(14, 6), nullable=False)
    CreditEL = Column(DECIMAL(14, 6), nullable=False)
    OperationRiskEl = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class RSYieldPerTenor(Base):
    __tablename__ = 'RS_YieldPerTenor'

    YieldPerTenorID = Column(Integer, primary_key=True)
    Yield = Column(DECIMAL(14, 6), nullable=False)
    LongTermMean = Column(DECIMAL(14, 6), nullable=False)
    TenorID = Column(Integer, nullable=False)
    FirstCoupon = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class RiskMeasure(Base):
    __tablename__ = 'RiskMeasure'

    RiskMeasureID = Column(Integer, primary_key=True)
    TradeDate = Column(DECIMAL(14, 2), nullable=False)
    IsinNumber = Column(Integer, nullable=False)
    PriceRisk1D = Column(DECIMAL(14, 2), nullable=False)
    PriceRisk10D = Column(DECIMAL(14, 2), nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDAuctionSetting(Base):
    __tablename__ = 'SD_AuctionSetting'

    AuctionSettingID = Column(Integer, primary_key=True)
    MmCommission = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDBondType(Base):
    __tablename__ = 'SD_BondType'

    BondTypeID = Column(Integer, primary_key=True)
    AmortisationType = Column(Unicode(50), nullable=False)
    IsFixed = Column(Boolean, nullable=False)
    Callable = Column(Boolean, nullable=False)
    IoPeriod = Column(Integer, nullable=False)
    TapPeriod = Column(Integer, nullable=False)
    DeviationLegalTenorAllowed = Column(Boolean, nullable=False)
    MaxDeviationBondTenor = Column(Integer, nullable=False)
    DeviationIoPeriodAllowed = Column(Boolean, nullable=False)
    MinIoPeriod = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDBookingEntry(Base):
    __tablename__ = 'SD_BookingEntries'

    BookingEntryID = Column(Integer, primary_key=True)
    EventNo = Column(Integer, nullable=False)
    Sign = Column(Unicode(1), nullable=False)
    Ledger = Column(Unicode(3), nullable=False)
    Account = Column(Integer, nullable=False)
    LoanProductID = Column(Integer, nullable=False)
    Version = Column(Integer, nullable=False)
    BookingEntryNo = Column(Integer, nullable=False)
    Scope = Column(Unicode(3), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDBookingEntryDescription(Base):
    __tablename__ = 'SD_BookingEntryDescription'

    BookingEntryDescriptionID = Column(Integer, primary_key=True)
    BookingEntryNo = Column(Integer, nullable=False)
    BookingEntryDescription = Column(Unicode)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDBucket(Base):
    __tablename__ = 'SD_Buckets'

    BucketID = Column(Integer, primary_key=True)
    Month = Column(Integer, nullable=False)
    Type = Column(Integer, nullable=False)
    Bucket = Column(Integer, nullable=False)
    BucketDescription = Column(Unicode(10))
    TimeStamp = Column(DateTime)


class SDCapitalisationParameter(Base):
    __tablename__ = 'SD_CapitalisationParameters'

    CapitalisationParameterID = Column(Integer, primary_key=True)
    ReportingDate = Column(Date, nullable=False)
    MarketRiskCapital = Column(DECIMAL(14, 6), nullable=False)
    OperationalRiskCapital = Column(DECIMAL(14, 6), nullable=False)
    OtherCapital = Column(DECIMAL(14, 6), nullable=False)
    LeverageRatio = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDCharterOfAccount(Base):
    __tablename__ = 'SD_CharterOfAccounts'

    CharterOfAccountID = Column(Integer, primary_key=True)
    Type = Column(Unicode(2), nullable=False)
    L1 = Column(Integer, nullable=False)
    L1_Description = Column(Unicode(50), nullable=False)
    L2 = Column(Integer, nullable=False)
    L2_Description = Column(Unicode(50), nullable=False)
    L3 = Column(Integer, nullable=False)
    L3_Description = Column(Unicode(50), nullable=False)
    L4 = Column(Integer, nullable=False)
    L4_Description = Column(Unicode(50), nullable=False)
    Account = Column(Integer, nullable=False)
    Account_Description = Column(Unicode(70), nullable=False)
    Centre = Column(Unicode(50), nullable=False)
    Ledger = Column(Unicode(50), nullable=False)
    System = Column(Unicode(50), nullable=False)
    Prototype = Column(Integer, nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDCodeblockMapping(Base):
    __tablename__ = 'SD_CodeblockMapping'

    CodeBlockMappingID = Column(Integer, primary_key=True)
    MappingSet = Column(Unicode(50), nullable=False)
    Account = Column(Integer, nullable=False)
    MapL1 = Column(Integer, nullable=False)
    MapL1desc = Column(Unicode(50), nullable=False)
    MapL2 = Column(Integer, nullable=False)
    MapL2desc = Column(Unicode(50), nullable=False)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDCustomerRate(Base):
    __tablename__ = 'SD_CustomerRate'

    CustomerRateID = Column(Integer, primary_key=True)
    CpMinimumChange = Column(DECIMAL(14, 6), nullable=False)
    CpMaximumChange = Column(DECIMAL(14, 6), nullable=False)
    CpAutoResumeTime = Column(Integer, nullable=False)
    cpPriceValidityPeriod = Column(Integer, nullable=False)
    cpBidSpread = Column(Integer, nullable=False)
    cpAskSpread = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDErc(Base):
    __tablename__ = 'SD_Erc'

    ErcId = Column(Integer, primary_key=True)
    Tenor = Column(Integer, nullable=False)
    ErcPercentage = Column(DECIMAL(14, 6), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDEvent(Base):
    __tablename__ = 'SD_Events'

    EventID = Column(Integer, primary_key=True)
    EventNo = Column(Integer, nullable=False)
    EventDescription = Column(Unicode)
    Version = Column(Integer, nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDHousePriceIndexation(Base):
    __tablename__ = 'SD_HousePriceIndexation'

    HousePriceIndexationId = Column(Integer, primary_key=True)
    EconomicScenarioID = Column(Integer, nullable=False)
    ReportingDate = Column(Date, nullable=False)
    HPI = Column(Float(53), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDLoanProduct(Base):
    __tablename__ = 'SD_LoanProduct'

    LoanProductID = Column(Integer, primary_key=True)
    BondTypeID = Column(Integer, nullable=False)
    Description = Column(Unicode(50), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDMarketMaker(Base):
    __tablename__ = 'SD_MarketMaker'

    MarketMakerID = Column(Integer, primary_key=True)
    Name = Column(Unicode(50), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDPortfolio(Base):
    __tablename__ = 'SD_Portfolio'

    PortfolioID = Column(Integer, primary_key=True)
    PortfolioName = Column(Unicode(50), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


class SDTenor(Base):
    __tablename__ = 'SD_Tenor'

    TenorID = Column(Integer, primary_key=True)
    Tenor = Column(Integer, nullable=False)
    Frequency = Column(Unicode(50), nullable=False)
    TimeStamp = Column(DateTime, nullable=False)


t_PyYieldIn = Table(
    'PyYieldIn', metadata,
    Column('Tenor', Float(53)),
    Column('Yield', Float(53))
)


t_PyYieldOut = Table(
    'PyYieldOut', metadata,
    Column('TenorID', Float(53)),
    Column('Yield', Float(53))
)