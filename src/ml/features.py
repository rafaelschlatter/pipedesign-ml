import pandas as pd

# A list of features that can be used during training or when doint predictions.
pipe_features = pd.core.indexes.base.Index(
    [
        'segment_1_X_End', 'segment_1_X_Start', 'segment_1_Y_End',
        'segment_1_Y_Start', 'segment_1_Z_End', 'segment_1_Z_Start',
        'segment_2_X_End', 'segment_2_X_Start', 'segment_2_Y_End',
        'segment_2_Y_Start', 'segment_2_Z_End', 'segment_2_Z_Start',
        'segment_3_X_End', 'segment_3_X_Start', 'segment_3_Y_End',
        'segment_3_Y_Start', 'segment_3_Z_End', 'segment_3_Z_Start',
        'segment_4_X_End', 'segment_4_X_Start', 'segment_4_Y_End',
        'segment_4_Y_Start', 'segment_4_Z_End', 'segment_4_Z_Start',
        'segment_5_X_End', 'segment_5_X_Start', 'segment_5_Y_End',
        'segment_5_Y_Start', 'segment_5_Z_End', 'segment_5_Z_Start',
        'segment_6_X_End', 'segment_6_X_Start', 'segment_6_Y_End',
        'segment_6_Y_Start', 'segment_6_Z_End', 'segment_6_Z_Start',
        'segment_7_X_End', 'segment_7_X_Start', 'segment_7_Y_End',
        'segment_7_Y_Start', 'segment_7_Z_End', 'segment_7_Z_Start',
        'segment_8_X_End', 'segment_8_X_Start', 'segment_8_Y_End',
        'segment_8_Y_Start', 'segment_8_Z_End', 'segment_8_Z_Start',
        'segment_9_X_End', 'segment_9_X_Start', 'segment_9_Y_End',
        'segment_9_Y_Start', 'segment_9_Z_End', 'segment_9_Z_Start'
    ],
        dtype='object'
)