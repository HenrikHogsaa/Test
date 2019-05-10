from decimal import Decimal
import datetime as dt
import db.models as model
import datedelta as dd
import math
import random
from scipy import stats


def generate_yield(yield_input, run_settings):

    yield_output = []
    first_date = run_settings[0].StartDate
    last_date = run_settings[0].EndDate
    run_date = first_date

    for i in range(len(yield_input)):
        tenor_id = yield_input[i].tenor_id
        bond_yield = Decimal(yield_input[i].eff_yield)
        long_term_mean = Decimal(yield_input[i].long_term_mean)
        reversion_to_mean = run_settings[0].ReversionToMean
        standard_dev = math.pow(run_settings[0].Volatility, 0.5)
        floor = run_settings[0].Floor
        cap = run_settings[0].Cap
        apply_reversion_to_mean = run_settings[0].ApplyReversionToMean
        if apply_reversion_to_mean:
            reversion = 1
        else:
            reversion = 0
        rate_before = Decimal(bond_yield)
        time_stamp = f'{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        run_date = first_date
        item = model.BondYield(id=None, bond_yield_date=run_date, bond_yield=round(bond_yield, 6), tenor_id= tenor_id,
                               time_stamp=time_stamp)
        yield_output.append(item)

        while run_date <= last_date:
            run_date = run_date + dt.timedelta(days=1)  # this method generates one bond price per tenor per day
            rnd = random.random()
            # a simple Garch process is applied
            # reversion to mean is only applied when set by the user
            factor = Decimal(stats.lognorm(standard_dev, 0).ppf(rnd))
            rate_after = round(rate_before * factor + ((long_term_mean - rate_before) * reversion * reversion_to_mean),
                               6)
            # rates should remain within user defined boundaries
            if rate_after >= cap:
                rate_after = cap
            elif rate_after <= floor:
                rate_after = floor

            item = model.BondYield(id=None, bond_yield_date=run_date, bond_yield=round(rate_after,6), tenor_id=tenor_id,
                                   time_stamp=time_stamp)
            yield_output.append(item)
            rate_before = rate_after

    return yield_output

def generate_isins(yield_input, run_settings, bond_yield):

    x = 2

    test = 1

    tmp = 0