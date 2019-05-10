import settings
from db import models
from db import helpers
from db import queries as q
from business_logic import bond_prices as bp
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
print(settings.BASE_DIR)

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine(settings.DATABASE_URI)

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()


# truncate all data tables
session.execute(q.truncate_BondPrice)
session.execute(q.truncate_BondYield)
session.execute(q.truncate_Isin)
session.execute(q.truncate_CustomerPrice)

# read all relevant data
yield_query = session.execute(q.get_viewYieldInput)
session.commit()
run_settings = session.query(models.RSBondPriceRunSetting).all()
session.commit()

# temporary step (see question on Wiki) - need to load the results from a normal SQL query into a named listed
yield_input = []
y_inp1 = helpers.YieldInput(18,300,'M',0.022, 0.024,0.0225)
y_inp2 = helpers.YieldInput(19,360,'M',0.023,0.025,.02250)
yield_input.append(y_inp1)
yield_input.append(y_inp2)

# generate yield
bond_price_table = bp.generate_yield(yield_input,run_settings)
session.add_all(bond_price_table)
session.commit()

# generate ISINS
isins_table = bp.generate_isins(yield_input,run_settings,bond_price_table)


# create a BondPrice
# bp = models.BondPrice(
#     BondPriceID=None,
#     Date=datetime.now(),
#     IsinNumber=1,
#     MarketMakerID=2,
#     Bid=3.14,
#     Ask=4.23,
#     Mid=3.73,
#     TimeStamp=datetime.now()
# )
# session.add(bp)
# session.commit()
#
# bond_prices = session.query(models.BondPrice).all()
# for bond_price in bond_prices:
#     print(f'ID: {bond_price.BondPriceID}')
#     print(f'Date: {bond_price.Date}')
#     print(f'IsInNumber: {bond_price.IsinNumber}')
#     print(f'MarketMakerID: {bond_price.MarketMakerID}')
#     print(f'Bid: {bond_price.Bid}')
#     print(f'Mid: {bond_price.Mid}')
#     print(f'Ask: {bond_price.Ask}')
#     print(f'TimeStamp: {bond_price.TimeStamp}')

# session.commit()

#