from client import EarnedMediaValueEconometricRoiSynthesizerClient

def main():
    client = EarnedMediaValueEconometricRoiSynthesizerClient()
    res = client.compute_campaign_emv_roi(5000000, 290000, 60000.00)
    print('EMV Econometric ROI Synthesizer: ' + res['econometric_report_id'])
    print('Earned Media Value: $' + str(res['earned_media_value_emv_usd']) + ' | Multiplier: ' + str(res['emv_multiplier_factor']) + 'x')
    print('Blended CAC: $' + str(res['blended_customer_acquisition_cost_cac_usd']) + ' | Significance: ' + str(res['brand_lift_statistical_significance_pct']) + '%')
    print('Dashboard URL: ' + res['executive_roi_dashboard_url'])

if __name__ == '__main__':
    main()
