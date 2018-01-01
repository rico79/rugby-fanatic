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
            },

            players: {
                player_10: {
                    id: 'player_10',
                    number: 10,
                    color: "grey darken-4",
                },
                player_15: {
                    id: 'player_15',
                    number: 15,
                    color: "grey darken-4",
                },
            },

            positions: {
                player_10: 'field_cell_10_11',
                field_cell_10_11: 'player_10',
                
                player_15: 'field_cell_10_10',
                field_cell_10_10: 'player_15',
            },
        },
    },

    getters: {
        getFieldCellId: (state) => (long, large) => {
            return 'field_cell_' + long + '_' + large
        },

        getPlayerInCell: (state) => (cellId) => {
            var playerId = state.stadium.positions[cellId]
            if (playerId) {
                return state.stadium.players[playerId]
            } else {
                return false
            }
        }
    },

    mutations: {
        playerMovesTo (state, move) {
            // Player quit position
            var playerFromCellId = state.stadium.positions[move.playerId]
            delete state.stadium.positions[playerFromCellId]

            // To new position
            state.stadium.positions[move.playerId] = move.cellId
            state.stadium.positions[move.cellId] = move.playerId
        },

        redesignStadium (state, stadiumSize) {
            // Set if vertical
            state.stadium.isVertical = (stadiumSize.width < stadiumSize.height)

            // Set field nb of cells
            var fieldVerticalCellNb, fieldHorizontalCellNb
            if (state.stadium.isVertical) {
                fieldVerticalCellNb = state.stadium.field.long
                fieldHorizontalCellNb = state.stadium.field.large
            } else {
                fieldHorizontalCellNb = state.stadium.field.long
                fieldVerticalCellNb = state.stadium.field.large
            }

            // Compute cell size
            state.stadium.cellSize = Math.min(
                Math.floor(stadiumSize.width / fieldHorizontalCellNb), 
                Math.floor(stadiumSize.height / fieldVerticalCellNb),
            )
        }
    },
}