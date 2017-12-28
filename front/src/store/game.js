// Game module
export default {
    state: {
        stadium: {            
            isVertical: false,          
            cellSize: 0,

            field: {
                long: 26, 
                large: 17,
                verticalCellNb: 0,
                horizontalCellNb: 0,
                image: 'rugby-field',
                imageURL: '',
            },
        },
    },

    mutations: {
        resizeStadium (state, stadiumSize) {
            // Set if vertical
            state.stadium.isVertical = (stadiumSize.width < stadiumSize.height)

            // Update field nb of cells and image URL
            if (state.stadium.isVertical) {
                state.stadium.field.verticalCellNb = state.stadium.field.long
                state.stadium.field.horizontalCellNb = state.stadium.field.large
                state.stadium.field.imageURL = 'url("/static/img/' + state.stadium.field.image + '-vertical.jpg")'
            } else {
                state.stadium.field.horizontalCellNb = state.stadium.field.long
                state.stadium.field.verticalCellNb = state.stadium.field.large
                state.stadium.field.imageURL = 'url("/static/img/' + state.stadium.field.image + '-horizontal.jpg")'
            }

            // Compute cell size
            state.stadium.cellSize = Math.min(
                Math.floor(stadiumSize.width / state.stadium.field.horizontalCellNb), 
                Math.floor(stadiumSize.height / state.stadium.field.verticalCellNb),
            )
        }
    },
}