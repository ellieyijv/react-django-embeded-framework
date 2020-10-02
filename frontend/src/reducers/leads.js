import { GET_LEADS, DELETE_LEAD, ADD_LEAD } from "../actions/types.js"

const initialState = {
    leads: []
}

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_LEADS:
            return {
                leads: action.payload
            };
        case DELETE_LEAD:
            return {
                leads: state.leads.filter(lead => lead.id !== action.payload)
            }
        case ADD_LEAD:
            return {
                leads: [...state.leads, action.payload]
            };
         default:
            return state;
    }
}