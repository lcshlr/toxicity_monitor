describe('Integration test', () => {
    it('Test connection with backend', () => {
      cy.request('http://localhost:5000')
       .should((response) => {
        expect(response.status).to.eq(200)
     })
    })
  });