// Game module
export default {
    state: {
        stadium: {            
            isVertical: false,          
            cellSize: 0,

            field: {
                long: 26, 
                large: 17,
                image: 'rugby-field',
                imageURL: '',
            },
        },
    },

    getters: {
        getFieldCellId: (state) => (long, large) => {
            return 'field_cell_' + long + '_' + large
        }
    },

    mutations: {
        redesignStadium (state, stadiumSize) {
            // Set if vertical
            state.stadium.isVertical = (stadiumSize.width < stadiumSize.height)

            // Set field nb of cells and update image URL
            var fieldVerticalCellNb, fieldHorizontalCellNb
            if (state.stadium.isVertical) {
                fieldVerticalCellNb = state.stadium.field.long
                fieldHorizontalCellNb = state.stadium.field.large
                state.stadium.field.imageURL = 'url("/static/img/' + state.stadium.field.image + '-vertical.jpg")'
            } else {
                fieldHorizontalCellNb = state.stadium.field.long
                fieldVerticalCellNb = state.stadium.field.large
                state.stadium.field.imageURL = 'url("/static/img/' + state.stadium.field.image + '-horizontal.jpg")'
            }

            // Compute cell size
            state.stadium.cellSize = Math.min(
                Math.floor(stadiumSize.width / fieldHorizontalCellNb), 
                Math.floor(stadiumSize.height / fieldVerticalCellNb),
            )
        }
    },
}